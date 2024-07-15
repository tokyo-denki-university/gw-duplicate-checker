import requests
from .router_info import get_router_name
from .config import WEBHOOK_URL


def send_notification(message):
    payload = {"text": message}
    response = requests.post(WEBHOOK_URL, json=payload)
    if response.status_code != 200:
        raise ValueError(
            f"Request to Mattermost returned an error {response.status_code}, the response is:\n{response.text}"
        )


def send_table(title, headers, rows):
    table = f"{title}\n\n"
    table += "| " + " | ".join(headers) + " |\n"
    table += "| " + " | ".join(["---"] * len(headers)) + " |\n"
    for row in rows:
        table += "| " + " | ".join(row) + " |\n"
    send_notification(table)


def notify_duplicates(duplicates):
    if duplicates:
        headers = ["IP Address", "MAC Addresses"]
        rows = []
        for ip, macs in duplicates.items():
            mac_names = [get_router_name(mac) for mac in macs]
            rows.append([ip, ", ".join(mac_names)])
        send_table("@channel\n🚫 重複したIPアドレスを持つデバイス", headers, rows)


def notify_devices(devices):
    if devices:
        headers = ["IP Address", "MAC Address", "Router"]
        rows = []
        for device in devices:
            mac = device["mac"]
            router_name = get_router_name(mac)
            rows.append([device["ip"], mac, router_name])
        send_table("✅ 現在検出しているデバイス", headers, rows)
