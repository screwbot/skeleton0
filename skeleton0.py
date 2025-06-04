#!/usr/bin/env python3

import subprocess
import random
import time
import os

# Spoof random ports by opening/closing dummy services
def spoof_random_ports(count=10):
    print("[*] Spoofing random ports...")
    for _ in range(count):
        port = random.randint(1025, 65535)
        subprocess.Popen(["nc", "-lk", str(port)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"[*] Spoofing port {port}")
        time.sleep(0.5)

# Set iptables firewall rules
def configure_firewall():
    print("[*] Setting up firewall rules...")
    rules = [
        "iptables -F",
        "iptables -X",
        "iptables -P INPUT DROP",
        "iptables -P FORWARD DROP",
        "iptables -P OUTPUT ACCEPT",
        "iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT",
        "iptables -A INPUT -p tcp --dport 22 -j ACCEPT",  # allow SSH for now
        "iptables -A INPUT -i lo -j ACCEPT"
    ]
    for rule in rules:
        subprocess.run(rule, shell=True)

# Start DNSCrypt-proxy for encrypted DNS queries
def start_dnscrypt_proxy():
    print("[*] Starting DNSCrypt-proxy for encrypted DNS...")
    subprocess.run("dnscrypt-proxy -config ./dnscrypt-proxy.toml", shell=True)

# Setup port knocking
def setup_port_knocking():
    print("[*] Setting up knockd...")
    subprocess.run("knockd -c ./knockd.conf -d", shell=True)

# Start Fail2Ban
def setup_fail2ban():
    print("[*] Starting Fail2Ban...")
    subprocess.run("systemctl start fail2ban", shell=True)

def main():
    spoof_random_ports()
    configure_firewall()
    setup_port_knocking()
    setup_fail2ban()
    start_dnscrypt_proxy()
    print("[+] Skeleton0 is running. Hardened and hidden.")

if __name__ == "__main__":
    main()
