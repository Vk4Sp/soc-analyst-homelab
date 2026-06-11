# Project 02 — Oracle Cloud VM Hardening

## Problem
A freshly provisioned Ubuntu VM on Oracle Cloud has default settings
that are not suitable for a production or lab environment exposed to
the internet. Goal: document and apply a hardening baseline.

## Environment
- Oracle Cloud Free Tier
- Ubuntu 22.04 LTS

## What I did
Step-by-step hardening log documented in `setup-log.md`:
- Enforced SSH key-only authentication (disabled password auth)
- Audited open ports using `ss -tulnp`
- Configured UFW firewall rules
- Disabled root login over SSH
- Reviewed and trimmed running services

## Status
🔧 In progress

## Skills demonstrated
`SSH hardening` `UFW` `systemd` `port auditing` `cloud security basics`
