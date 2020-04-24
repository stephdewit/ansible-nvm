import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_node(host):
    r = host.run('. ~/.bashrc && node -v')
    assert r.succeeded
    assert r.stderr == ''

def test_nvm(host):
    r = host.run('. ~/.bashrc && nvm --version')
    assert r.succeeded
    assert r.stderr == ''
