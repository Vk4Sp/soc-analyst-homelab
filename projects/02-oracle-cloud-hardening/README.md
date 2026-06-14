# Oracle Cloud VM Hardening

## Overview

This project focuses on auditing and hardening an Ubuntu virtual machine hosted on Oracle Cloud Infrastructure (OCI). The objective was to identify unnecessary services, exposed ports, firewall rules, user privileges, and SSH configuration issues that could increase the attack surface of the system.

## Objectives

* Understand Linux service management using systemd
* Audit open network ports and listening services
* Review user accounts and administrative privileges
* Analyze firewall configuration using UFW
* Investigate Docker workloads and container usage
* Review SSH authentication settings
* Apply basic hardening measures

## Environment

* Cloud Provider: Oracle Cloud Infrastructure (OCI)
* Operating System: Ubuntu 22.04 LTS
* Access Method: SSH Key Authentication

## Audit Areas

### Port Audit

Reviewed listening TCP and UDP ports using system networking tools.

### Service Audit

Identified active services and investigated their purpose.

### User and Privilege Audit

Reviewed local accounts, group memberships, and sudo privileges.

### Firewall Audit

Examined inbound and outbound firewall policies and reviewed open ports.

### SSH Security Audit

Verified authentication methods and remote access configuration.

### Docker Investigation

Investigated Docker services, images, and containers to determine whether they were still required.

## Key Findings

* Legacy RustDesk deployment artifacts remained on the system.
* Docker services were enabled despite no active containers being used.
* RPC, iSCSI, and multipath-related services remained enabled from previous experiments.
* Firewall rules associated with RustDesk remained open even though the service was no longer in use.
* SSH password authentication was disabled and public key authentication was enabled.

## Hardening Actions Performed

* Disabled Docker service
* Disabled rpcbind service
* Disabled iscsid service
* Disabled multipathd service
* Removed obsolete UFW firewall rules
* Verified SSH key-based authentication configuration

## Skills Demonstrated

* Linux Administration
* Service Management
* System Auditing
* Firewall Configuration
* SSH Security
* Docker Investigation
* Security Hardening
* Cloud Infrastructure Operations

## Results

The hardening audit identified legacy services and firewall rules from a previous RustDesk deployment.

Actions taken:

- Disabled Docker service
- Disabled RPCBind service
- Disabled iSCSI service
- Disabled Multipath service
- Removed obsolete firewall rules
- Verified SSH key-based authentication

Outcome:

- Reduced attack surface
- Reduced unnecessary startup services
- Improved firewall posture
- Maintained secure remote administration through SSH keys

## Future Improvements

* Remove unused packages after validation
* Implement centralized log monitoring
* Configure automated compliance checks
* Add audit automation scripts
* Explore intrusion detection and monitoring tools
