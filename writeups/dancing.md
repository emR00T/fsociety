<p align="center">

# 💃 HackTheBox — Dancing Write-up

<img src="https://img.shields.io/badge/HackTheBox-Starting%20Point-9FEF00?style=for-the-badge&logo=hackthebox">
<img src="https://img.shields.io/badge/Platform-Windows-blue?style=for-the-badge&logo=windows">
<img src="https://img.shields.io/badge/Difficulty-Very%20Easy-success?style=for-the-badge">
<img src="https://img.shields.io/badge/Category-SMB-orange?style=for-the-badge">
<img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge">

</p>

---

# 📖 Overview

| Category | Information |
|-----------|-------------|
| Machine | Dancing |
| Platform | Hack The Box |
| Difficulty | ⭐ Very Easy |
| Operating System | Windows |
| Main Topic | SMB Enumeration |

---

# 🎯 Objective

This machine introduces the fundamentals of Windows network enumeration through the SMB (Server Message Block) protocol.

The objective is to identify accessible resources, review available network shares, and understand how insecure share permissions can expose sensitive information.

---

# 🌐 Reconnaissance

Initial reconnaissance identified several Microsoft networking services.

## Service Discovery

| Port | State | Service |
|------|:----:|---------|
| 135 | Open | MSRPC |
| 139 | Open | NetBIOS Session Service |
| 445 | Open | Microsoft-DS (SMB) |
| 5985 | Open | WinRM |

The presence of SMB services indicates that network shares should be examined during the assessment.

---

# 🔍 Findings

Enumeration of the SMB service revealed an accessible network share named **WorkShares**.

Reviewing accessible files within this share led to the discovery of the challenge flag inside the **James.J** directory.

This demonstrates how excessive file-sharing permissions can unintentionally expose sensitive information.

---

# 🔓 Initial Access

Access to the available network share allowed navigation through its contents.

No privilege escalation or code execution was required to complete the machine; the primary objective was achieved through proper service enumeration and review of accessible files.

---

# 🏁 Flag

The challenge flag was successfully located within the shared directory, completing the machine.

---

# 🔄 Attack Flow

```text
Reconnaissance
      │
      ▼
SMB Service Discovery
      │
      ▼
Share Enumeration
      │
      ▼
Accessible Files
      │
      ▼
Flag Retrieved
```

---

# 🛡 Security Issues

| Issue | Risk |
|--------|------|
| Overly Permissive SMB Shares | Unauthorized access to files |
| Weak Share Permissions | Information disclosure |
| Insufficient Access Control | Sensitive data exposure |
| Poor Permission Management | Increased attack surface |

---

# ✅ Mitigations

To reduce the risk of similar issues:

- Apply the principle of least privilege to SMB shares.
- Regularly review share permissions.
- Restrict anonymous or unnecessary access.
- Store sensitive information only in protected locations.
- Enable logging and auditing for file access.
- Periodically remove unused network shares.

---

# 📚 Key Takeaways

- SMB enumeration is an important step during Windows assessments.
- Misconfigured file shares can expose confidential information.
- Proper access control is essential for protecting shared resources.
- Regular permission audits help reduce unnecessary exposure.

---

# 🧠 Skills Learned

- Windows Service Enumeration
- SMB Enumeration
- Network Share Analysis
- Information Disclosure Assessment
- Windows File Sharing Concepts
- Security Misconfiguration Identification

---

# 📈 Machine Summary

| Category | Result |
|----------|:------:|
| Enumeration | ✅ |
| Service Discovery | ✅ |
| SMB Assessment | ✅ |
| Information Gathering | ✅ |
| Flag Captured | ✅ |

---

<p align="center">

## 🟩 Machine Completed

*"Properly configured permissions are one of the strongest layers of defense."*

<img src="https://img.shields.io/badge/Write--up-Completed-success?style=for-the-badge">
<img src="https://img.shields.io/badge/Windows-SMB-blue?style=for-the-badge">
<img src="https://img.shields.io/badge/fsociety-Learning-red?style=for-the-badge">

</p>