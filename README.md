nvm
========

Install nvm and Node.js.

Requirements
------------

git, curl, build-essential, libssl-dev. Requirements are installed by the role.

Role Variables
--------------

* `nvm.version` nvm version tag, or `HEAD`. Defaults to `v0.4.0`
* `nvm.node_version` Node.js version. Defaults to `'0.10.'`

Dependencies
------------

No depedencies.

Example Playbook
-------------------------

    - hosts: servers
      roles:
        - role: stephdewit.nvm
          nvm:
            version: v0.4.0
            node_version: '0.10'

License
-------

BSD

Author Information
------------------

Jarno Keskikangas
