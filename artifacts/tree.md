/lynis # tree -a -L 4
.
|-- .git
|   |-- HEAD
|   |-- branches
|   |-- config
|   |-- description
|   |-- hooks
|   |   |-- applypatch-msg.sample
|   |   |-- commit-msg.sample
|   |   |-- fsmonitor-watchman.sample
|   |   |-- post-update.sample
|   |   |-- pre-applypatch.sample
|   |   |-- pre-commit.sample
|   |   |-- pre-merge-commit.sample
|   |   |-- pre-push.sample
|   |   |-- pre-rebase.sample
|   |   |-- pre-receive.sample
|   |   |-- prepare-commit-msg.sample
|   |   |-- push-to-checkout.sample
|   |   |-- sendemail-validate.sample
|   |   `-- update.sample
|   |-- index
|   |-- info
|   |   `-- exclude
|   |-- logs
|   |   |-- HEAD
|   |   `-- refs
|   |       |-- heads
|   |       `-- remotes
|   |-- objects
|   |   |-- info
|   |   `-- pack
|   |       |-- pack-d56040a72cc1a897f64319f0e7cda562dcf0c5a1.idx
|   |       |-- pack-d56040a72cc1a897f64319f0e7cda562dcf0c5a1.pack
|   |       `-- pack-d56040a72cc1a897f64319f0e7cda562dcf0c5a1.rev
|   |-- packed-refs
|   `-- refs
|       |-- heads
|       |   `-- master
|       |-- remotes
|       |   `-- origin
|       `-- tags
|-- .github
|   `-- ISSUE_TEMPLATE
|       |-- bug_report.md
|       `-- feature_request.md
|-- .gitignore
|-- .travis.yml
|-- CHANGELOG.md
|-- CODE_OF_CONDUCT.md
|-- CONTRIBUTING.md
|-- CONTRIBUTORS.md
|-- FAQ
|-- HAPPY_USERS.md
|-- INSTALL
|-- LICENSE
|-- README
|-- README.md
|-- SECURITY.md
|-- TODO.md
|-- db
|   |-- fileperms.db
|   |-- hints.db
|   |-- integrity.db
|   |-- languages
|   |   |-- az
|   |   |-- br -> pt
|   |   |-- cn
|   |   |-- da
|   |   |-- de
|   |   |-- de-AT -> de
|   |   |-- en
|   |   |-- en-GB -> en
|   |   |-- en-US -> en
|   |   |-- es
|   |   |-- fi
|   |   |-- fr
|   |   |-- gr
|   |   |-- he
|   |   |-- hu
|   |   |-- id
|   |   |-- it
|   |   |-- ja
|   |   |-- ko
|   |   |-- nb-NO
|   |   |-- nl
|   |   |-- nl-BE -> nl
|   |   |-- nl-NL -> nl
|   |   |-- pl
|   |   |-- pt
|   |   |-- ru
|   |   |-- se
|   |   |-- sk
|   |   `-- tr
|   |-- malware-susp.db
|   |-- malware.db
|   |-- sbl.db
|   |-- software-eol.db
|   `-- tests.db
|-- default.prf
|-- developer.prf
|-- extras
|   |-- README
|   |-- bash_completion.d
|   |   `-- lynis
|   |-- build-lynis.sh
|   |-- check-lynis.sh
|   |-- files.dat
|   |-- lynis.spec
|   |-- openbsd
|   |   `-- +CONTENTS
|   |-- systemd
|   |   |-- lynis.service
|   |   `-- lynis.timer
|   `-- travis-ci
|       `-- before_script.sh
|-- include
|   |-- binaries
|   |-- consts
|   |-- data_upload
|   |-- functions
|   |-- helper_audit_dockerfile
|   |-- helper_configure
|   |-- helper_generate
|   |-- helper_show
|   |-- helper_system_remote_scan
|   |-- helper_update
|   |-- osdetection
|   |-- parameters
|   |-- profiles
|   |-- report
|   |-- tests_accounting
|   |-- tests_authentication
|   |-- tests_banners
|   |-- tests_boot_services
|   |-- tests_containers
|   |-- tests_crypto
|   |-- tests_custom.template
|   |-- tests_databases
|   |-- tests_dns
|   |-- tests_file_integrity
|   |-- tests_file_permissions
|   |-- tests_filesystems
|   |-- tests_firewalls
|   |-- tests_hardening
|   |-- tests_homedirs
|   |-- tests_insecure_services
|   |-- tests_kernel
|   |-- tests_kernel_hardening
|   |-- tests_ldap
|   |-- tests_logging
|   |-- tests_mac_frameworks
|   |-- tests_mail_messaging
|   |-- tests_malware
|   |-- tests_memory_processes
|   |-- tests_nameservices
|   |-- tests_networking
|   |-- tests_php
|   |-- tests_ports_packages
|   |-- tests_printers_spoolers
|   |-- tests_scheduling
|   |-- tests_shells
|   |-- tests_snmp
|   |-- tests_squid
|   |-- tests_ssh
|   |-- tests_storage
|   |-- tests_storage_nfs
|   |-- tests_system_integrity
|   |-- tests_time
|   |-- tests_tooling
|   |-- tests_usb
|   |-- tests_virtualization
|   |-- tests_webservers
|   `-- tool_tips
|-- lynis
|-- lynis.8
`-- plugins
    |-- README
    |-- custom_plugin.template
    |-- plugin_pam_phase1
    `-- plugin_systemd_phase1

28 directories, 153 files