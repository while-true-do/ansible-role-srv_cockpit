import os

import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("name", [
    ("cockpit-system"),
    ("cockpit-pcp"),
    ("cockpit-docker"),
    ("cockpit-machines"),
    ("cockpit-ws"),
    ("cockpit-dashboard"),
    ("cockpit-kubernetes"),
])
def test_pkg(host, name):
    pkg = host.package(name)
    assert pkg.is_installed


def test_srv(host):
    srv = host.service('cockpit.socket')
    assert srv.is_running
    assert srv.is_enabled


def test_socket(host):
    sock = host.socket('tcp://9090')
    assert sock.is_listening
