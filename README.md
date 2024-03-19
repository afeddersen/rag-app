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

## Configuration and settings

To gather more information about the configuration and settings of the wolfi-base container image that are relevant to the general purpose operating system STIG, you can run the following shell commands inside the container:

1. Check the version and release information:
   ```
   cat /etc/os-release
   uname -a
   ```

2. List installed packages:
   ```
   apk info
   ```

3. Check user and group information:
   ```
   cat /etc/passwd
   cat /etc/group
   cat /etc/shadow
   ```

4. Check sudo configuration:
   ```
   cat /etc/sudoers
   ls -l /etc/sudoers.d
   ```

5. Check SSH configuration (if SSH server is installed):
   ```
   cat /etc/ssh/sshd_config
   ```

6. Check network configuration:
   ```
   ip addr
   cat /etc/hosts
   cat /etc/resolv.conf
   ```

7. Check running processes:
   ```
   ps aux
   ```

8. Check open ports and network connections:
   ```
   netstat -tulpn
   ```

9. Check system logs:
   ```
   cat /var/log/messages
   cat /var/log/syslog
   cat /var/log/auth.log
   ```

10. Check file system mount points and permissions:
    ```
    mount
    ls -ld / /etc /var /usr /home
    ```

11. Check system security settings:
    ```
    cat /etc/security/limits.conf
    cat /etc/sysctl.conf
    sysctl -a
    ```

12. Check installed services and their status:
    ```
    ls /etc/init.d
    ls /etc/systemd/system
    ```

13. Check system auditing configuration (if auditd is installed):
    ```
    cat /etc/audit/auditd.conf
    cat /etc/audit/audit.rules
    ```

Please note that some of these commands may not produce output or may not be applicable if the corresponding files, packages, or services are not present in the minimal wolfi-base image.

By running these commands and providing the output, you can give me more context about the system configuration, installed packages, user and group settings, network configuration, running processes, and security settings. This information will help me better understand the wolfi-base image's compliance with the general purpose operating system STIG.

Feel free to run these commands and share the relevant output, and I'll be happy to analyze it and provide further guidance on building your STIG checklist validator tool.

