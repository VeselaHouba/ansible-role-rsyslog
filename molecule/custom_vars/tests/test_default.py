import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_config_1(host):
    file = host.file("/etc/rsyslog.d/some-remote-host.conf")
    assert file.exists
    assert file.contains('some-remote-host.tld:514')
    assert file.contains('ActionQueueMaxDiskSpace')
    assert not file.contains('ActionExecOnlyWhenPreviousIsSuspended')


def test_config_2(host):
    file = host.file("/etc/rsyslog.d/mutli-remote-hosts.conf")
    assert file.exists
    assert file.contains('ActionExecOnlyWhenPreviousIsSuspended')
    assert not file.contains('ActionQueueMaxDiskSpace')
