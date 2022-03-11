import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_config_exists(host):
    file = host.file("/etc/rsyslog.d/some-remote-host.conf")
    assert file.exists
    assert file.contains('some-remote-host.tld:514')
    assert file.contains('ActionQueueMaxDiskSpace')


def test_config_contains_setting(host):
    file = host.file("/etc/rsyslog.d/some-remote-host.conf")
    assert file.exists
