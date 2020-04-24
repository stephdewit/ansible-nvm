import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_node(host):
    r = host.run('. ~/.bashrc && node -v')
    assert r.rc == 0
    assert r.succeeded
    assert r.stdout == 'v12.16.1\n'
    assert r.stderr == ''

def test_nvm(host):
    r = host.run('. ~/.bashrc && nvm --version')
    assert r.rc == 0
    assert r.succeeded
    assert r.stdout == '0.35.3\n'
    assert r.stderr == ''
