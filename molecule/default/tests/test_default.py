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
])
def test_cockpit_pkg(host, name):
    pkg = host.package(name)

    assert pkg.is_installed


def test_cockpit_web_srv(host):
    srv = host.service('cockpit.socket')

    assert srv.is_running
    assert srv.is_enabled


def test_cockpit_web_conf(host):
    file = host.file('/etc/cockpit/cockpit.conf')

    assert file.exists
    assert file.user == 'root'
    assert file.group == 'root'


def test_cockpit_web_socket(host):
    sock = host.socket('tcp://9090')

    assert sock.is_listening


def test_cockpit_web_clients(host):
    file = host.file('/etc/cockpit/machines.d/99-webui.json')

    assert file.exists
    assert file.user == 'root'
    assert file.group == 'root'
    assert file.contains('192.168.0.10')
    assert file.contains('host2')
    assert file.contains('host3.example.com')
