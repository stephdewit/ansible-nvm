nvm
========

Install nvm and Node.js.

Requirements
------------

git, curl, build-essential, libssl-dev. Requirements are installed by the role.

Role Variables
--------------

* `nvm_version` nvm version tag, or `HEAD`. Defaults to `0.33.1`
* `nvm_node_version` Node.js version. Defaults to `6.10.0`
* `nvm_install_path` nvm folder path. Defaults to `~/.nvm`

Dependencies
------------

No depedencies.

Example Playbook
-------------------------

    - hosts: servers
      roles:
        - role: stephdewit.nvm
          nvm_version: 0.4.0
          nvm_node_version: 0.10

License
-------

BSD

Author Information
------------------

Jarno Keskikangas
