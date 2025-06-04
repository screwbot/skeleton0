````markdown
# Skeleton0

**Skeleton0** is a lightweight, self-contained system hardening tool designed to obfuscate, protect, and defend Linux servers against basic and automated network attacks.

## 🛡️ Features

- 🔒 Port spoofing (random dummy ports to confuse scanners)
- 🕵️ Port knocking to hide SSH or sensitive services
- 🔥 Custom iptables firewall (deny by default)
- 🚫 Brute-force protection with Fail2Ban

## 🧰 Requirements

- Ubuntu/Debian (or similar Linux)
- `netcat`, `iptables`, `knockd`, `fail2ban`

Install dependencies with:

```bash
sudo apt install netcat iptables knockd fail2ban
````

## 🚀 Usage

```bash
sudo python3 skeleton0.py
```

## 🔐 Setup Notes

* `knockd.conf`: Defines the knock sequence (edit as needed)
* `fail2ban/jail.local`: Configures protection for SSH
* `iptables`: Default deny-all policy except loopback and SSH (if port knocked)

## ⚠️ Warning

This script is designed for **learning and lab environments**. Use at your own risk and adjust configurations to suit your production server's needs.

## 📜 License
`/LICENCE.md`
