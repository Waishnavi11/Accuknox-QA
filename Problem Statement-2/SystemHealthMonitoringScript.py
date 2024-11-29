import psutil
import logging

CPU_THRESHOLD = 80  
MEMORY_THRESHOLD = 80 
DISK_THRESHOLD = 80  
PROCESS_COUNT_THRESHOLD = 300 

logging.basicConfig(
    filename='system_health.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_alert(message):
    print(message)
    logging.warning(message)

def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        log_alert(f"ALERT: High CPU usage detected! Usage: {cpu_usage}%")

def check_memory():
    memory = psutil.virtual_memory()
    if memory.percent > MEMORY_THRESHOLD:
        log_alert(f"ALERT: High Memory usage detected! Usage: {memory.percent}%")

def check_disk():
    disk = psutil.disk_usage('/')
    if disk.percent > DISK_THRESHOLD:
        log_alert(f"ALERT: High Disk usage detected! Usage: {disk.percent}%")

def check_processes():
    process_count = len(psutil.pids())
    if process_count > PROCESS_COUNT_THRESHOLD:
        log_alert(f"ALERT: High number of processes detected! Count: {process_count}")

def monitor_system():
    logging.info("System Health Check Started")
    check_cpu()
    check_memory()
    check_disk()
    check_processes()
    logging.info("System Health Check Completed")

if __name__ == "__main__":
    while True:
        monitor_system()
