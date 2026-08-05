<p align="center">

# 🐊 HackTheBox — Crocodile Write-up

<img src="https://img.shields.io/badge/HackTheBox-Starting%20Point-9FEF00?style=for-the-badge&logo=hackthebox">
<img src="https://img.shields.io/badge/Platform-Linux-blue?style=for-the-badge&logo=linux">
<img src="https://img.shields.io/badge/Difficulty-Easy-success?style=for-the-badge">
<img src="https://img.shields.io/badge/Category-FTP%20%26%20Web-orange?style=for-the-badge">
<img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge">

</p>

---

# 📖 Overview

| Category | Information |
|-----------|-------------|
| Machine | Crocodile |
| Platform | Hack The Box |
| Difficulty | ⭐ Easy |
| Operating System | Linux |
| Main Topics | FTP, Web Authentication |

---

# 🎯 Objective

This machine focuses on identifying exposed services, recognizing insecure configurations, and understanding how information disclosure can affect web application security.

---

# 🌐 Reconnaissance

Initial reconnaissance identified the following exposed network services.

## Service Discovery

| Port | State | Service |
|------|:----:|---------|
| 21 | Open | FTP |
| 80 | Open | HTTP |

The combination of FTP and a web application suggests that multiple services should be reviewed during the assessment.

---

# 🔍 Findings

During the assessment, the FTP service exposed information that could be used during the authentication process of the web application.

This demonstrates how insecure configurations on one service can unintentionally expose data relevant to another.

---

# 🔓 Initial Access

Information obtained from the available services was sufficient to authenticate successfully to the web application.

After successful authentication, access to the challenge flag was obtained.

---

# 🏁 Flag

The flag was successfully retrieved after authenticating to the web application, completing the machine.

---

# 🔄 Attack Flow

```text
Reconnaissance
      │
      ▼
FTP Service Discovery
      │
      ▼
Information Disclosure
      │
      ▼
Web Authentication
      │
      ▼
Flag Retrieved
```

---

# 🛡 Security Issues

| Issue | Risk |
|--------|------|
| Anonymous FTP Access | Unauthorized information disclosure |
| Sensitive Files Exposed | Credential leakage |
| Weak Access Control | Increased attack surface |
| Poor Credential Management | Unauthorized application access |

---

# ✅ Mitigations

To reduce the risk of similar issues:

- Disable anonymous FTP access unless absolutely necessary.
- Avoid storing sensitive information in publicly accessible locations.
- Apply the principle of least privilege.
- Use strong, unique credentials.
- Regularly audit exposed services and file permissions.
- Monitor authentication and file access logs.
- Remove unnecessary services from production systems.

---

# 📚 Key Takeaways

- Every exposed service should be assessed individually.
- Information disclosure can significantly increase overall risk.
- Anonymous access should be disabled whenever possible.
- Sensitive files should never be publicly accessible.
- Secure configuration is as important as secure code.

---

# 🧠 Skills Learned

- Service Enumeration
- FTP Assessment
- Web Application Assessment
- Information Disclosure Analysis
- Authentication Concepts
- Security Misconfiguration Identification

---

# 📈 Machine Summary

| Category | Result |
|----------|:------:|
| Enumeration | ✅ |
| Service Discovery | ✅ |
| Information Gathering | ✅ |
| Web Authentication | ✅ |
| Flag Captured | ✅ |

---

<p align="center">

## 🟩 Machine Completed

*"Small misconfigurations can lead to significant security exposure."*

<img src="https://img.shields.io/badge/Write--up-Completed-success?style=for-the-badge">
<img src="https://img.shields.io/badge/FTP-Security-blue?style=for-the-badge">
<img src="https://img.shields.io/badge/fsociety-Learning-red?style=for-the-badge">

</p>