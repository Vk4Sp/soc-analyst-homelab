# Linux System Health Monitoring Tool

## Overview

A Python-based Linux monitoring tool developed on Oracle Cloud Infrastructure (OCI) using Ubuntu 22.04 LTS. The tool collects key system health metrics and generates timestamped reports for monitoring and troubleshooting purposes.

## Features

* CPU Usage Monitoring
* Memory Usage Monitoring
* Disk Usage Monitoring
* System Uptime Tracking
* Health Status Classification (OK / WARNING / CRITICAL)
* Process Count Monitoring
* Top CPU Process Identification
* Top Memory Process Identification
* Linux Load Average Monitoring
* Timestamped Report Generation

## Technologies Used

* Python 3
* psutil
* Linux (Ubuntu 22.04)
* Oracle Cloud Infrastructure (OCI)
* Git & GitHub

## Sample Output

See:

sample-output/report_sample.txt

## How to Run

```bash
python3 monitor.py
```

## Example Use Cases

* Basic Linux System Monitoring
* Infrastructure Health Checks
* Troubleshooting Resource Utilization
* Learning Linux Administration Concepts

## Future Enhancements

* Service Health Monitoring
* Email Alerting
* Dashboard Visualization
* Scheduled Report Generation
