from datetime import datetime
import socket
import psutil
import os


def get_status(value, warning_threshold, critical_threshold):
    if value >= critical_threshold:
        return "CRITICAL"
    elif value >= warning_threshold:
        return "WARNING"
    else:
        return "OK"


def get_overall_status(statuses):
    if "CRITICAL" in statuses:
        return "CRITICAL"
    elif "WARNING" in statuses:
        return "WARNING"
    else:
        return "HEALTHY"


# Timestamp and Hostname
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
filename_timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

hostname = socket.gethostname()

# System Metrics
cpu_usage = psutil.cpu_percent(interval=1)
memory_usage = psutil.virtual_memory().percent
disk_usage = psutil.disk_usage('/').percent

# Uptime
boot_time = datetime.fromtimestamp(psutil.boot_time())
uptime = datetime.now() - boot_time

days = uptime.days
hours, remainder = divmod(uptime.seconds, 3600)
minutes, _ = divmod(remainder, 60)

uptime_string = f"{days} days, {hours} hours, {minutes} minutes"

# Status Classification
cpu_status = get_status(cpu_usage, 70, 90)
memory_status = get_status(memory_usage, 70, 90)
disk_status = get_status(disk_usage, 80, 90)

overall_status = get_overall_status(
    [cpu_status, memory_status, disk_status]
)

# Report Content
report = f"""
==================================================
Linux System Health Report
==================================================

Timestamp : {timestamp}
Hostname  : {hostname}

OVERALL STATUS : {overall_status}

CPU Usage    : {cpu_usage}% ({cpu_status})
Memory Usage : {memory_usage}% ({memory_status})
Disk Usage   : {disk_usage}% ({disk_status})

System Uptime:
{uptime_string}

==================================================
"""

# Print to terminal
print(report)

# Save report
report_dir = "logs/reports"
os.makedirs(report_dir, exist_ok=True)

report_file = f"{report_dir}/report_{filename_timestamp}.txt"

with open(report_file, "w") as file:
    file.write(report)

print(f"Report saved: {report_file}")
