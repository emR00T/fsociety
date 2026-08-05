<p align="center">

# 🦌 HackTheBox — Fawn Write-up

<img src="https://img.shields.io/badge/HackTheBox-Starting%20Point-9FEF00?style=for-the-badge&logo=hackthebox">
<img src="https://img.shields.io/badge/Platform-Linux-blue?style=for-the-badge&logo=linux">
<img src="https://img.shields.io/badge/Difficulty-Very%20Easy-success?style=for-the-badge">
<img src="https://img.shields.io/badge/Category-FTP-orange?style=for-the-badge">
<img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge">

</p>

---

# 📖 Overview

| Category | Information |
|-----------|-------------|
| Machine | Fawn |
| Platform | Hack The Box |
| Difficulty | ⭐ Very Easy |
| Operating System | Linux |
| Main Topic | FTP |

---

# 🎯 Objective

This machine introduces the basics of **FTP (File Transfer Protocol)** enumeration and demonstrates the security risks associated with anonymous FTP access.

The goal is to identify exposed services, assess FTP configuration, and understand how misconfigured file-sharing services can expose sensitive information.

---

# 🌐 Reconnaissance

The first phase of the assessment focused on identifying available network services.

## Service Discovery

| Port | State | Service | Version |
|------|:----:|---------|---------|
| 21 | Open | FTP | vsftpd 3.0.3 |

The scan identified an FTP service running on the target system, making it the primary focus of the assessment.

---

# 🔍 Findings

Further analysis revealed that the FTP server allowed **anonymous authentication**.

Allowing anonymous users to browse or download files is generally considered an insecure configuration unless carefully restricted.

---

# 🔓 Initial Access

Anonymous access to the FTP service provided access to publicly available files.

During the review of accessible content, the challenge flag was successfully located.

No privilege escalation or additional exploitation was required.

---

# 🏁 Flag

The flag was retrieved successfully from the FTP server, completing the challenge.

---

# 🔄 Attack Flow

```text
Reconnaissance
      │
      ▼
FTP Service Discovery
      │
      ▼
Anonymous Access
      │
      ▼
File Enumeration
      │
      ▼
Flag Retrieved
```

---

# 🛡 Security Issues

| Issue | Risk |
|--------|------|
| Anonymous FTP Access | Unauthorized file access |
| Sensitive Files Stored on FTP | Information disclosure |
| Weak Service Configuration | Increased attack surface |
| Improper File Permissions | Confidential data exposure |

---

# ✅ Mitigations

To reduce the risk of similar issues:

- Disable anonymous FTP access unless absolutely required.
- Store sensitive files in protected locations.
- Enforce proper authentication for all users.
- Apply the principle of least privilege.
- Regularly audit FTP permissions and accessible directories.
- Replace FTP with secure alternatives such as SFTP or FTPS whenever possible.

---

# 📚 Key Takeaways

- FTP services should always be reviewed during reconnaissance.
- Anonymous access can unintentionally expose sensitive information.
- Secure file transfer protocols should be preferred over traditional FTP.
- Proper permission management significantly reduces security risks.

---

# 🧠 Skills Learned

- Service Enumeration
- FTP Enumeration
- Anonymous Access Assessment
- File Discovery
- Information Disclosure Analysis
- Security Misconfiguration Identification

---

# 📈 Machine Summary

| Category | Result |
|----------|:------:|
| Enumeration | ✅ |
| Service Discovery | ✅ |
| FTP Assessment | ✅ |
| Information Gathering | ✅ |
| Flag Captured | ✅ |

---

<p align="center">

## 🟩 Machine Completed

*"Small configuration mistakes can lead to major security risks."*

<img src="https://img.shields.io/badge/Write--up-Completed-success?style=for-the-badge">
<img src="https://img.shields.io/badge/FTP-Security-blue?style=for-the-badge">
<img src="https://img.shields.io/badge/fsociety-Learning-red?style=for-the-badge">

</p>