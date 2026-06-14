# Oracle Cloud VM Hardening Project

## Objective

To understand how Linux servers expose services, identify unnecessary attack surface, and apply basic hardening practices on an Oracle Cloud Ubuntu VM.

---

## Environment

Cloud Provider: Oracle Cloud Infrastructure (OCI)

Operating System: Ubuntu 22.04 LTS

Purpose:
Personal cloud security and Linux administration lab.

---

## Audit Methodology

1. Identify open ports.
2. Identify running services.
3. Identify unnecessary services.
4. Review users and permissions.
5. Review firewall configuration.
6. Review SSH security.
7. Apply hardening actions.
8. Document findings and recommendations.

## Port Audit

Command Used:

ss -tulnp

Purpose:

Identify listening TCP and UDP ports and determine which services are exposed.

Findings:

Port 22/TCP
Service: SSH

Reason:
Used for remote administration of the VM.

Status:
Required.

---

Port 53/TCP, UDP
Service: systemd-resolved (DNS)

Reason:
Used for hostname resolution.

Status:
Required.

---

Port 68/UDP
Service: DHCP Client

Reason:
Obtains network configuration from Oracle Cloud.

Status:
Required.

---

Port 111/TCP, UDP
Service: rpcbind

Reason:
RPC service mapping.

Status:
Requires further investigation.

## Service Audit

Command Used:

systemctl list-units --type=service --state=running

Purpose:

Identify active background services and determine whether they are required.

Observations:

Essential Services:
- ssh
- systemd-networkd
- systemd-resolved
- systemd-timesyncd
- rsyslog
- cron

Reason:
Required for system operation and remote administration.

---

Potentially Unnecessary Services:
- rpcbind
- docker
- iscsid
- multipathd
- packagekit
- udisks2

Reason:
Need verification before removal.

## Docker Investigation

Commands Used:

docker images
docker ps -a

Findings:

Docker service is active.

Stored image:
- rustdesk/rustdesk-server

Containers:
- hbbs (stopped)
- hbbr (stopped)

Both containers have been inactive for approximately two months.

Assessment:

Docker may no longer be required if RustDesk is not actively used.

Recommendation:

Verify whether RustDesk is still needed before removing Docker-related components.

## User Audit

Command Used:

cat /etc/passwd

Purpose:

Identify user accounts present on the system and classify them.

Findings:

Human Accounts:
- root
- ubuntu
- opc

System Accounts:
- daemon
- bin
- sys
- nobody

Service Accounts:
- sshd
- systemd-network
- systemd-resolve
- syslog
- tcpdump
- _rpc

Observations:

Most service accounts are configured with /usr/sbin/nologin, preventing interactive logins.

Further Investigation:

Determine whether the opc account is still required.

## Privilege Audit

Commands Used:

id
sudo -l

Purpose:

Determine user identity, group memberships, and administrative privileges.

Findings:

User:
- ubuntu (UID 1001)

Important Groups:
- sudo
- adm
- netdev
- lxd

Privilege Assessment:

The ubuntu account has full administrative privileges through sudo.

The account is configured with:

NOPASSWD: ALL

meaning administrative commands can be executed without entering a password.

Risk:

If the ubuntu account is compromised, an attacker could obtain full system control.

Status:

Acceptable for a personal lab environment.

## Firewall Audit

Command Used:

sudo ufw status verbose

Purpose:

Review inbound and outbound firewall policies.

Findings:

Default Policy:
- Incoming: Deny
- Outgoing: Allow
- Routed: Deny

Allowed Inbound Ports:
- 443
- 21115
- 21116
- 21117

Assessment:

The firewall follows a secure default-deny model.

However, several inbound ports remain open that appear related to a historical RustDesk deployment.

Recommendation:

Verify whether RustDesk is still required. If not, remove the associated firewall rules.


### SSH Authentication Review

Configuration File:
- /etc/ssh/sshd_config.d/60-cloudimg-settings.conf

Finding:
- PasswordAuthentication no

Assessment:
Password-based SSH login is disabled.

Security Benefit:
Reduces the risk of brute-force and credential-stuffing attacks.

Current Access Method:
SSH public key authentication.

Status:
Good practice.

## Hardening Recommendations

### Docker

Finding:
Docker is enabled but no active containers are running.

Recommendation:
Disable the Docker service if container workloads are no longer required.

---

### RPCBind

Finding:
RPCBind is enabled and exposes port 111.

Recommendation:
Disable if NFS and RPC services are not required.

---

### iSCSI

Finding:
iSCSI service is enabled but no remote storage is in use.

Recommendation:
Disable.

---

### Multipath

Finding:
Multipath service is enabled but enterprise storage paths are not in use.

Recommendation:
Disable.

## Final Findings

### Finding 1: Legacy RustDesk Deployment

Evidence:

* RustDesk Docker image present.
* RustDesk containers stopped for approximately two months.
* Firewall ports 443, 21115, 21116 and 21117 remained open.
* Docker service remained enabled.

Risk:
Unnecessary services and open firewall rules increased attack surface.

Action Taken:

* Disabled Docker service.
* Removed obsolete firewall rules.

Result:
Reduced externally exposed attack surface.

---

### Finding 2: Unused Infrastructure Services

Evidence:

* rpcbind, iscsid and multipathd services enabled.
* No active use of RPC, NFS, iSCSI or multipath storage.

Action Taken:

* Disabled unused services.

Result:
Reduced number of active services and boot-time processes.

---

### Finding 3: SSH Configuration

Evidence:

* PasswordAuthentication set to no.
* PubkeyAuthentication enabled.
* Root login restricted to key-based authentication.

Assessment:
Current SSH configuration follows recommended cloud security practices.

---

## Conclusion

A security audit of an Oracle Cloud Ubuntu VM was performed. Open ports, running services, user accounts, privileges, firewall rules, Docker workloads and SSH configuration were reviewed. Legacy services and firewall rules from a previous RustDesk deployment were identified and disabled. The final system configuration reduced unnecessary attack surface while maintaining secure remote administration through SSH key authentication.
