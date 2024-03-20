# Working with wolfi-base

docker run -it --entrypoint /bin/sh cgr.dev/chainguard/wolfi-base:latest

## Generate an SBOM

```
syft cgr.dev/chainguard/wolfi-base:latest -o cyclonedx > wolfi-base.xml
```

## Generate a directory structure

```
apk add tree
```

```
tree -a -L 4 / > /directory_structure.txt
```

https://github.com/afeddersen/rag-app/blob/main/artifacts/dod.md
etc_apk_arch.md
etc_apk_keys_wolfi-signing.rsa.pub.md
etc_apk_repositories.md
etc_apk_world.md
etc_busybox-paths.d_busybox.md
etc_group.md
etc_host.conf.md
etc_hostname.md
etc_hosts.md
etc_ld.so.conf.md
etc_nsswitch.conf.md
etc_os-release.md
etc_passwd.md
etc_profile.d_locale.sh.md
etc_profile.md
etc_protocols.md
etc_resolv.conf.md
etc_rpc.md
etc_secfixes.d_wolfi.md
etc_securetty.md
etc_services.md
etc_shadow.md
etc_shells.md
etc_ssl_certs_ca-certificates.crt.md
etc_ssl_ct_log_list.cnf.dist.md
etc_ssl_ct_log_list.cnf.md
etc_ssl_misc_CA.pl.md
etc_ssl_misc_tsget.pl.md
etc_ssl_openssl.cnf.dist.md
etc_ssl_openssl.cnf.md
lynis.md
stig-overview.md
tree.md
