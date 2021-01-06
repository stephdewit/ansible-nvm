nvm
===

[![Build Status](https://travis-ci.org/stephdewit/ansible-nvm.svg?branch=master)](https://travis-ci.org/stephdewit/ansible-nvm)

Install nvm and Node.js.

Requirements
------------

git, curl, build-essential, libssl-dev. Requirements are installed by the role.

Role Variables
--------------

* `nvm_version` nvm version tag, or `HEAD` | `master` | `latest`. Defaults to `0.37.2`
* `nvm_node_version` Node.js specific version `12.16.0` or use `lts` | `latest`. Defaults to `14.15.4`
* `nvm_install_path` nvm folder path, support absolute and relative path. Defaults to `~/.nvm`
* `nvm_shell_init_file` The Shell initialization file to add sourcing of NVM to. Defaults to `~/.profile`
* `nvm_force_install` **Boolean**. Force reinstall nvm from git, for example if you change some files in `nvm_install_path`. Defaults to `false`
* `nvm_install_deps` **Boolean**. Allow to skip dependencies setup and therefore run as a non-root user. Defaults to `true`

Dependencies
------------

No dependencies.

Example Playbook
----------------

    - hosts: servers
      roles:
        - role: stephdewit.nvm
          nvm_version: 0.4.0
          nvm_node_version: 0.10

Install latest version always

    - hosts: servers
      roles:
        - role: stephdewit.nvm
          nvm_version: 'latest'
          nvm_node_version: 'latest'

When run with another user than the logged one, it may help to set `NVM_DIR` environment variable to an absolute path:

    - hosts: servers
      roles:
        - role: stephdewit.nvm
          become: yes
          become_user: vagrant
          environment:
            NVM_DIR: /home/vagrant/.nvm

License
-------

BSD

Author Information
------------------

- Jarno Keskikangas
- [Stéphane de Wit](https://www.stephanedewit.be)
