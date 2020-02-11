nvm
===

Install nvm and Node.js.

Requirements
------------

git, curl, build-essential, libssl-dev. Requirements are installed by the role.

Role Variables
--------------

* `nvm_version` nvm version tag, or `HEAD`. Defaults to `0.35.2`
* `nvm_node_version` Node.js version. Defaults to `12.16.0`
* `nvm_install_path` nvm folder path. Defaults to `~/.nvm`
* `nvm_shell_init_file` The Shell initialization file to add sourcing of NVM to. Defaults to `~/.profile`

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
