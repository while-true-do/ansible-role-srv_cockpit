<!--
name: README.md
description: This file contains important information for the repository.
author: while-true-do.io
contact: hello@while-true-do.io
license: BSD-3-Clause
-->

<!-- github shields -->
[![Github (tag)](https://img.shields.io/github/tag/while-true-do/ansible-role-srv_cockpit.svg)](https://github.com/while-true-do/ansible-role-srv_cockpit/tags)
[![Github (license)](https://img.shields.io/github/license/while-true-do/ansible-role-srv_cockpit.svg)](https://github.com/while-true-do/ansible-role-srv_cockpit/blob/master/LICENSE)
[![Github (issues)](https://img.shields.io/github/issues/while-true-do/ansible-role-srv_cockpit.svg)](https://github.com/while-true-do/ansible-role-srv_cockpit/issues)
[![Github (pull requests)](https://img.shields.io/github/issues-pr/while-true-do/ansible-role-srv_cockpit.svg)](https://github.com/while-true-do/ansible-role-srv_cockpit/pulls)
<!-- travis shields -->
[![Travis (com)](https://img.shields.io/travis/com/while-true-do/ansible-role-srv_cockpit.svg)](https://travis-ci.com/while-true-do/ansible-role-srv_cockpit)
<!-- ansible shields -->
[![Ansible (min. version)](https://img.shields.io/badge/dynamic/yaml.svg?label=Min.%20Ansible%20Version&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-srv_cockpit%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.min_ansible_version&colorB=black)](https://galaxy.ansible.com/while_true_do/srv_cockpit)
[![Ansible (platforms)](https://img.shields.io/badge/dynamic/yaml.svg?label=Supported%20OS&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-srv_cockpit%2Fmaster%2Fmeta%2Fmain.yml&query=galaxy_info.platforms%5B*%5D.name&colorB=black)](https://galaxy.ansible.com/while_true_do/srv_cockpit)
[![Ansible (tags)](https://img.shields.io/badge/dynamic/yaml.svg?label=Galaxy%20Tags&url=https%3A%2F%2Fraw.githubusercontent.com%2Fwhile-true-do%2Fansible-role-srv_cockpit%2Fmaster%2Fmeta%2Fmain.yml&query=%24.galaxy_info.galaxy_tags%5B*%5D&colorB=black)](https://galaxy.ansible.com/while_true_do/srv_cockpit)

# Ansible Role: srv_cockpit

An Ansible role to install and configure Cockpit.

## Motivation

[Cockpit](https://cockpit-project.org/) ia a very interesting management tool
for Linux servers. It does provide an overview of different metrics and allows
management for several features. It does integrate with tools like
[docker](https://www.docker.com/),
[selinux](https://selinuxproject.org/page/Main_Page), kdump,
[podman](https://podman.io/) or [kvm](https://www.linux-kvm.org/page/Main_Page).

## Description

This role installs and configures several features and modules of cockpit.

-   cockpit system
-   cockpit web
-   integration for docker
-   integration for libvirt
-   integration for performance co-pilot
-   integration for podman
-   configure the dashboard
-   configure firewalld

## Requirements

There are no hard requirements. Nevertheless, since cockpit integrates with
lots of services, you should review some of these tools and optional roles.

Optional Roles:

-   [while_true_do.srv_docker](https://github.com/while-true-do/ansible-role-srv_docker)
-   [while_true_do.srv_kvm](https://github.com/while-true-do/ansible-role-srv_kvm)
-   [while_true_do.srv_pcp](https://github.com/while-true-do/ansible-role-srv_pcp)
-   [while_true_do.srv_podman](https://github.com/while-true-do/ansible-role-srv_podman)
-   [while_true_do.sys_kdump](https://github.com/while-true-do/ansible-role-sys_kdump)
-   [while_true_do.sys_selinux](https://github.com/while-true-do/ansible-role-sys_selinux)
-   [while_true_do.sys_tuned](https://github.com/while-true-do/ansible-role-sys_tuned)

Used Modules:

-   [Ansible Package Module](https://docs.ansible.com/ansible/latest/modules/package_module.html)
-   [Ansible Service Module](https://docs.ansible.com/ansible/latest/modules/service_module.html)
-   [Ansible Template Module](https://docs.ansible.com/ansible/latest/modules/template_module.html)
-   [Ansible Firewalld Module](https://docs.ansible.com/ansible/latest/modules/firewalld_module.html)
-   [Ansible RHSM Repository Module](https://docs.ansible.com/ansible/latest/modules/rhsm_repository_module.html)

## Installation

Install from [Ansible Galaxy](https://galaxy.ansible.com/while_true_do/srv_cockpit)
```
ansible-galaxy install while_true_do.srv_cockpit
```

Install from [Github](https://github.com/while-true-do/ansible-role-srv_cockpit)
```
git clone https://github.com/while-true-do/ansible-role-srv_cockpit.git while_true_do.srv_cockpit
```

Dependencies:

If you want to install all optional roles, run the below command.

```
ansible-galaxy install -r requirements.yml
```

## Usage

### Role Variables

```
---
# defaults file for while_true_do.srv_cockpit

## Package Management
# Defaults are based on Fedora Linux

# Cockpit System Packages
# Most likely needed for all systems
# You should consider to have a look at:
# - while_true_do.sys_kdump
# - while_true_do.sys_selinux
# - while_true_do.sys_tuned
wtd_srv_cockpit_sys_package:
  - cockpit-networkmanager
  - cockpit-storaged
  - cockpit-sosreport
  - cockpit-system
  - cockpit-kdump
  - cockpit-selinux
# State can be present|latest|absent|unmanaged
wtd_srv_cockpit_sys_package_state: "present"

# Cockpit Packagekit Integration
wtd_srv_cockpit_pk_package:
  - cockpit-packagekit
# State can be present|latest|absent|unmanaged
wtd_srv_cockpit_pk_package_state: "present"

# Cockpit PCP Integration
# You should consider to look at while_true_do.sys_pcp
wtd_srv_cockpit_pcp_package:
  - cockpit-pcp
# State can be present|latest|absent|unmanaged
wtd_srv_cockpit_pcp_package_state: "present"

# Cockpit Docker Integration
# You should consider to look at while_true_do.srv_docker
wtd_srv_cockpit_docker_package:
  - cockpit-docker
# State can be present|latest|absent|unmanaged
wtd_srv_cockpit_docker_package_state: "absent"

# Cockpit Podman Integration
# You should consider to look at while_true_do.srv_podman
wtd_srv_cockpit_podman_package:
  - cockpit-podman
# State can be present|latest|absent|unmanaged
wtd_srv_cockpit_podman_package_state: "absent"

# Cockpit libvirt Integration
# You should consider to look at while_true_do.srv_kvm
wtd_srv_cockpit_machines_package:
  - cockpit-machines
# State can be present|latest|absent|unmanaged
wtd_srv_cockpit_machines_package_state: "absent"

## Cockpit Web Management
# Only needed, if you want to access the server directly via web ui

# Cockpit Web Package Management
wtd_srv_cockpit_web_package:
  - cockpit
  - cockpit-ws
# State can be present|latest|absent|unmanaged
wtd_srv_cockpit_web_package_state: "absent"

# Cockpit Web Dashboard for multiple servers
wtd_srv_cockpit_web_dash_package:
  - cockpit-dashboard
# State can be present|latest|absent|unmanaged
wtd_srv_cockpit_web_dash_package_state: "absent"

## Cockpit Web Service Management
wtd_srv_cockpit_web_service: "cockpit.socket"
# State can be started|stopped
wtd_srv_cockpit_web_service_state: "started"
wtd_srv_cockpit_web_service_enabled: true

## Cockpit Web Firewalld Management
wtd_srv_cockpit_web_fw_mgmt: true
wtd_srv_cockpit_web_fw_service: "cockpit"
# State can be enabled|disabled
wtd_srv_cockpit_web_fw_service_state: "enabled"
# Zone can be according to defined zones on your machine.
wtd_srv_cockpit_web_fw_service_zone: "public"

## Cockpit Web Configuration Management
# See here: http://cockpit-project.org/guide/latest/cockpit.conf.5.html
wtd_srv_cockpit_web_conf_Origins: ""
wtd_srv_cockpit_web_conf_ProtocolHeader: ""
wtd_srv_cockpit_web_conf_LoginTo: ""
wtd_srv_cockpit_web_conf_LoginTitle: ""
wtd_srv_cockpit_web_conf_RequireHost: ""
wtd_srv_cockpit_web_conf_MaxStartups: "3"
wtd_srv_cockpit_web_conf_AllowUnencrypted: ""
wtd_srv_cockpit_web_conf_UrlRoot: ""
# See here: http://cockpit-project.org/guide/latest/cockpit-ws.8.html
wtd_srv_cockpit_web_conf_cert: ""

# wtd_srv_cockpit_web_conf_clients:
#   - name: "host1.example.com"   # ip|fqdn
#     color: "rgb(0, 0, 255)"     # defaults to random color
#     port: "22"                  # defaults to 22
```

### Example Playbook

Running Ansible
[Roles](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html)
can be done in a
[playbook](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html).

#### Simple

```
---
- hosts: all
  roles:
    - role: while_true_do.srv_cockpit
```

#### Host with web interface and dashboard

```
- hosts: all
  roles:
    - role: while_true_do.srv_cockpit
      wtd_srv_cockpit_web_package_state: "present"
      wtd_srv_cockpit_web_dash_package_state: "present"
```

#### Add multiple Clients to the Dashboard

```
- hosts: all
  roles:
    - role: while_true_do.srv_cockpit
      wtd_srv_cockpit_web_package_state: "present"
      wtd_srv_cockpit_web_dash_package_state: "present"
      wtd_srv_cockpit_web_conf_clients:
        - name: "host1"
          address: "host1.example.com"
        - name: "host2"
          address: "host2.example.com"
        - name: "host3"
          address: "192.168.22.10"
```

## Known Issues

1.  RedHat Testing is currently not possible in public, due to limitations
    in subscriptions.
2.  Some services and features cannot be tested properly, due to limitations
    in docker.

## Testing

Most of the "generic" tests are located in the
[Test Library](https://github.com/while-true-do/test-library).

Ansible specific testing is done with
[Molecule](https://molecule.readthedocs.io/en/stable/).

Infrastructure testing is done with
[testinfra](https://testinfra.readthedocs.io/en/stable/).

Automated testing is done with [Travis CI](https://travis-ci.com/while-true-do).

## Contribute

Thank you so much for considering to contribute. We are very happy, when somebody
is joining the hard work. Please fell free to open
[Bugs, Feature Requests](https://github.com/while-true-do/ansible-role-srv_cockpit/issues)
or [Pull Requests](https://github.com/while-true-do/ansible-role-srv_cockpit/pulls) after
reading the [Contribution Guideline](https://github.com/while-true-do/doc-library/blob/master/docs/CONTRIBUTING.md).

See who has contributed already in the [kudos.txt](./kudos.txt).

## License

This work is licensed under a [BSD-3-Clause License](https://opensource.org/licenses/BSD-3-Clause).

## Contact

-   Site <https://while-true-do.io>
-   Twitter <https://twitter.com/wtd_news>
-   Code <https://github.com/while-true-do>
-   Mail [hello@while-true-do.io](mailto:hello@while-true-do.io)
-   IRC [freenode, #while-true-do](https://webchat.freenode.net/?channels=while-true-do)
-   Telegram <https://t.me/while_true_do>
