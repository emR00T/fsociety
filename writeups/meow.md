<p align="center">

# 🐱 HackTheBox — Meow Write-up

<img src="https://img.shields.io/badge/HackTheBox-Starting%20Point-9FEF00?style=for-the-badge&logo=hackthebox">
<img src="https://img.shields.io/badge/Platform-Linux-blue?style=for-the-badge&logo=linux">
<img src="https://img.shields.io/badge/Difficulty-Very%20Easy-success?style=for-the-badge">
<img src="https://img.shields.io/badge/Service-Telnet-orange?style=for-the-badge">
<img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge">

</p>

---

# 📖 Overview

| Category | Information |
|-----------|-------------|
| Machine | Meow |
| Platform | Hack The Box |
| Difficulty | ⭐ Very Easy |
| Operating System | Linux |
| Main Service | Telnet |
| Skills Practiced | Enumeration, Service Identification, Authentication |

---

# 🎯 Objective

The goal of this machine is to:

- Perform basic reconnaissance
- Identify exposed services
- Access the Telnet service
- Obtain the user shell
- Retrieve the flag
- Understand why insecure remote access services should never be exposed

---

# 🌐 Reconnaissance

The first step is identifying open ports and running services.

### Nmap Scan

```bash
nmap -sV -T4 TARGET_IP
```

### Scan Result

| Port | State | Service | Version |
|------|:----:|---------|---------|
| 23 | Open | Telnet | Linux telnetd |

### Analysis

The scan reveals that **Telnet (port 23)** is publicly accessible.

Since Telnet transmits credentials in plain text and lacks encryption, it is considered an insecure protocol and has largely been replaced by SSH.

---

# 🔑 Initial Access

After discovering the Telnet service, connect to the target:

```bash
telnet TARGET_IP
```

The machine allows login using the **root** account without a password.

Once authenticated, a root shell is immediately available.

---

# 🏁 Flag Retrieval

After obtaining shell access, locate and read the flag.

```bash
cat /root/flag.txt
```

The flag confirms successful completion of the machine.

---

# 🔍 Attack Flow

```text
Port Scan
      │
      ▼
Service Enumeration
      │
      ▼
Telnet Login
      │
      ▼
Root Access
      │
      ▼
Read Flag
```

---

# 🛡 Security Issues

This machine demonstrates several common security misconfigurations.

| Issue | Risk |
|--------|------|
| Telnet Enabled | Credentials transmitted without encryption |
| Root Login Allowed | Full administrative access |
| Empty Password | Unauthorized access becomes trivial |
| Insecure Remote Access | Complete system compromise |

---

# ✅ Mitigations

To improve security:

- Disable Telnet completely.
- Replace Telnet with SSH.
- Disable direct root login.
- Enforce strong password policies.
- Use multi-factor authentication where possible.
- Restrict remote administration to trusted networks.
- Monitor authentication logs.
- Apply regular system updates.

---

# 📚 Key Takeaways

✅ Perform service enumeration before exploitation.

✅ Open ports often reveal the attack surface.

✅ Telnet should never be exposed on production systems.

✅ Root accounts should never allow passwordless access.

✅ Secure remote administration should always use SSH.

---

# 🧠 Skills Learned

- Basic Enumeration
- Nmap Scanning
- Service Identification
- Telnet Usage
- Linux Basics
- Authentication Concepts
- Security Misconfiguration Analysis

---

# 📈 Machine Summary

| Category | Result |
|----------|:------:|
| Enumeration | ✅ |
| Service Discovery | ✅ |
| Initial Access | ✅ |
| Root Access | ✅ |
| Flag Captured | ✅ |

---

<p align="center">

## 🟩 Machine Completed

*"Every solved machine is another step toward becoming a better security professional."*

<img src="https://img.shields.io/badge/Write--up-Completed-success?style=for-the-badge">
<img src="https://img.shields.io/badge/fsociety-Learning-red?style=for-the-badge">

</p>