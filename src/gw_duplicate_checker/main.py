import time
from .mattermost import notify_duplicates, notify_devices
from .network_scan import scan_network, check_for_duplicate_ips


def periodic_scan(ip_range, interval):
    while True:
        devices = scan_network(ip_range)
        if devices:
            notify_devices(devices)
        time.sleep(interval)


def duplicate_check(ip_range, interval):
    while True:
        devices = scan_network(ip_range)
        duplicates = check_for_duplicate_ips(devices)
        if duplicates:
            notify_duplicates(duplicates)
        time.sleep(interval)
