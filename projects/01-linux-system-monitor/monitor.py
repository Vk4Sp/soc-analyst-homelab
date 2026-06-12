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

load1, load5, load15 = os.getloadavg()

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

# Process Monitoring

process_count = len(psutil.pids())

top_cpu_process = None
top_memory_process = None

processes = []

for proc in psutil.process_iter(['pid', 'name']):
    try:
        cpu = proc.cpu_percent(interval=0.1)
        memory = proc.memory_percent()

        processes.append({
            'pid': proc.info['pid'],
            'name': proc.info['name'],
            'cpu': cpu,
            'memory': memory
        })

    except (psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess):
        pass

if processes:
    top_cpu_process = max(processes, key=lambda p: p['cpu'])
    top_memory_process = max(processes, key=lambda p: p['memory'])

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

Load Average:
1 min  : {load1:.2f}
5 min  : {load5:.2f}
15 min : {load15:.2f}

Total Processes:
{process_count}

Top CPU Process:
{top_cpu_process['name']} (PID: {top_cpu_process['pid']})
CPU Usage: {top_cpu_process['cpu']:.2f}%

Top Memory Process:
{top_memory_process['name']} (PID: {top_memory_process['pid']})
Memory Usage: {top_memory_process['memory']:.2f}%

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
