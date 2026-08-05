<p align="center">

# 💰 HackTheBox — Redeemer Write-up

<img src="https://img.shields.io/badge/HackTheBox-Starting%20Point-9FEF00?style=for-the-badge&logo=hackthebox">
<img src="https://img.shields.io/badge/Platform-Linux-blue?style=for-the-badge&logo=linux">
<img src="https://img.shields.io/badge/Difficulty-Very%20Easy-success?style=for-the-badge">
<img src="https://img.shields.io/badge/Category-Redis-orange?style=for-the-badge">
<img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge">

</p>

---

# 📖 Overview

| Category | Information |
|-----------|-------------|
| Machine | Redeemer |
| Platform | Hack The Box |
| Difficulty | ⭐ Very Easy |
| Operating System | Linux |
| Main Topic | Redis |

---

# 🎯 Objective

This machine introduces the fundamentals of **Redis enumeration** and demonstrates the risks associated with insecure database configurations.

The objective is to identify the exposed Redis service, examine the available data, and understand why databases should never be left accessible without proper authentication.

---

# 🌐 Reconnaissance

Initial reconnaissance identified an exposed Redis service.

## Service Discovery

| Port | State | Service |
|------|:----:|---------|
| 6379 | Open | Redis |

Redis is an in-memory key-value database commonly used for caching, session storage, and high-performance applications.

---

# 🔍 Findings

Further assessment showed that the Redis instance was accessible without authentication.

An exposed Redis service can allow unauthorized users to enumerate stored data if proper security controls are not in place.

---

# 🔓 Initial Access

A connection to the Redis service was successfully established.

After reviewing the available key-value data, the challenge flag was identified and retrieved.

---

# 🏁 Flag

The flag was successfully recovered from the Redis database, completing the challenge.

---

# 🔄 Attack Flow

```text
Reconnaissance
      │
      ▼
Redis Service Discovery
      │
      ▼
Database Enumeration
      │
      ▼
Stored Data Review
      │
      ▼
Flag Retrieved
```

---

# 🛡 Security Issues

| Issue | Risk |
|--------|------|
| Redis Accessible Without Authentication | Unauthorized database access |
| Publicly Exposed Database | Information disclosure |
| Weak Security Configuration | Increased attack surface |
| Missing Access Controls | Unauthorized data retrieval |

---

# ✅ Mitigations

To reduce the risk of similar issues:

- Enable authentication for Redis instances.
- Restrict network access using firewalls.
- Avoid exposing Redis directly to the public Internet.
- Use strong credentials and access control policies.
- Encrypt communication where appropriate.
- Monitor database access logs and unusual activity.
- Keep Redis updated with the latest security patches.

---

# 📚 Key Takeaways

- Databases should never be exposed without proper authentication.
- Redis is frequently deployed for performance but must be securely configured.
- Limiting network exposure greatly reduces risk.
- Regular security reviews help identify misconfigurations before they become vulnerabilities.

---

# 🧠 Skills Learned

- Service Enumeration
- Redis Identification
- Database Enumeration
- Information Disclosure Analysis
- Security Misconfiguration Assessment
- Secure Database Configuration Concepts

---

# 📈 Machine Summary

| Category | Result |
|----------|:------:|
| Enumeration | ✅ |
| Service Discovery | ✅ |
| Redis Assessment | ✅ |
| Information Gathering | ✅ |
| Flag Captured | ✅ |

---

<p align="center">

## 🟩 Machine Completed

*"A secure service begins with a secure configuration."*

<img src="https://img.shields.io/badge/Write--up-Completed-success?style=for-the-badge">
<img src="https://img.shields.io/badge/Redis-Security-red?style=for-the-badge">
<img src="https://img.shields.io/badge/fsociety-Learning-black?style=for-the-badge">

</p>