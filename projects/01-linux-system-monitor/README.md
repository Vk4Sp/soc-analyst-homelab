# Project 01 — Linux System Monitor

## Problem
No visibility into the health of a running Ubuntu server without manually
running individual commands. Needed a single script to collect and report
system state automatically.

## Environment
- Oracle Cloud Free Tier (VM.Standard.E2.1.Micro)
- Ubuntu 22.04 LTS
- Python 3.10

## What I built
A Python script (`monitor.py`) that collects:
- CPU and memory usage
- Disk utilization
- Active network connections (via `ss`)
- Running systemd services
- Last 5 login attempts

Output is written to a timestamped report file under `sample-output/`.

## Status
🔧 In progress

## Skills demonstrated
`Python` `Linux CLI` `systemd` `ss` `ps` `cron` `log reading`
