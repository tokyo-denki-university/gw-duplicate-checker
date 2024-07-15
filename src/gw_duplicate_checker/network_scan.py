import scapy.all as scapy


def scan_network(ip_range):
    arp_request = scapy.ARP(pdst=ip_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    devices = []
    for element in answered_list:
        devices.append({"ip": element[1].psrc, "mac": element[1].hwsrc})

    return devices


def check_for_duplicate_ips(devices):
    ip_mac_mapping = {}
    duplicates = {}

    for device in devices:
        ip = device["ip"]
        mac = device["mac"]
        if ip in ip_mac_mapping:
            ip_mac_mapping[ip].append(mac)
        else:
            ip_mac_mapping[ip] = [mac]

    for ip, macs in ip_mac_mapping.items():
        if len(macs) > 1:
            duplicates[ip] = macs

    return duplicates
