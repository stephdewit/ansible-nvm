nvm
===

Install nvm and Node.js.

Requirements
------------

git, curl, build-essential, libssl-dev. Requirements are installed by the role.

Role Variables
--------------

* `nvm_version` nvm version tag, or `HEAD`. Defaults to `0.35.0`
* `nvm_node_version` Node.js version. Defaults to `12.13.0`
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
          nvm_shell_init_file: ~/.bashrc

License
-------

BSD

Author Information
------------------

- Jarno Keskikangas
- [Stéphane de Wit](https://www.stephanedewit.be)
