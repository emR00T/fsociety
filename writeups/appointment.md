<p align="center">

# 🌐 HackTheBox — Appointment Write-up

<img src="https://img.shields.io/badge/HackTheBox-Starting%20Point-9FEF00?style=for-the-badge&logo=hackthebox">
<img src="https://img.shields.io/badge/Platform-Web-blue?style=for-the-badge">
<img src="https://img.shields.io/badge/Difficulty-Very%20Easy-success?style=for-the-badge">
<img src="https://img.shields.io/badge/Category-SQL%20Injection-orange?style=for-the-badge">
<img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge">

</p>

---

# 📖 Overview

| Category | Information |
|-----------|-------------|
| Machine | Appointment |
| Platform | Hack The Box |
| Difficulty | ⭐ Very Easy |
| Category | Web Security |
| Primary Topic | SQL Injection |

---

# 🎯 Objective

The purpose of this machine is to understand:

- Basic web application enumeration
- Authentication mechanisms
- SQL Injection fundamentals
- Common authentication bypass vulnerabilities
- Secure coding practices

---

# 🌐 Reconnaissance

The initial reconnaissance identified a web service running on the target.

### Service Discovery

| Port | State | Service | Version |
|------|:----:|---------|---------|
| 80 | Open | HTTP | Apache Web Server |

The web application presents a login page, making authentication the primary attack surface for this challenge.

---

# 🔍 Vulnerability Analysis

Testing the login form reveals that the authentication logic is vulnerable to **SQL Injection**.

The vulnerability allows specially crafted input to alter the behavior of the underlying SQL query, resulting in successful authentication without valid credentials.

---

# 🔓 Initial Access

After exploiting the vulnerable authentication mechanism, access to the application is granted and the challenge flag becomes available.

This demonstrates how improper handling of user input can compromise an entire application.

---

# 🏁 Flag

Once authenticated successfully, the machine displays the flag, marking the challenge as completed.

---

# 🔄 Attack Flow

```text
Port Scan
      │
      ▼
HTTP Service Identified
      │
      ▼
Login Page Analysis
      │
      ▼
SQL Injection
      │
      ▼
Authentication Bypass
      │
      ▼
Flag Retrieved
```

---

# 🛡 Security Issues

| Issue | Risk |
|--------|------|
| SQL Injection | Authentication bypass |
| Unsanitized User Input | Arbitrary SQL execution |
| Weak Authentication Logic | Unauthorized access |
| Missing Input Validation | Increased attack surface |

---

# ✅ Mitigations

To prevent vulnerabilities like this:

- Use **prepared statements (parameterized queries)**.
- Never concatenate user input directly into SQL queries.
- Validate and sanitize all user input.
- Apply the principle of least privilege to database accounts.
- Implement proper authentication and error handling.
- Perform regular security testing and code reviews.

---

# 📚 Key Takeaways

- SQL Injection remains one of the most common web application vulnerabilities.
- Authentication forms should always be tested securely during assessments.
- Secure database interaction requires parameterized queries.
- Proper input validation is a critical defense layer.
- Following secure coding practices significantly reduces risk.

---

# 🧠 Skills Learned

- Web Enumeration
- HTTP Service Identification
- Login Page Analysis
- SQL Injection Fundamentals
- Authentication Concepts
- Secure Coding Awareness

---

# 📈 Machine Summary

| Category | Result |
|----------|:------:|
| Enumeration | ✅ |
| Service Discovery | ✅ |
| Vulnerability Identification | ✅ |
| Authentication Bypass | ✅ |
| Flag Captured | ✅ |

---

<p align="center">

## 🟩 Machine Completed

*"Understanding vulnerabilities is the first step toward building secure applications."*

<img src="https://img.shields.io/badge/Write--up-Completed-success?style=for-the-badge">
<img src="https://img.shields.io/badge/Web-Security-blue?style=for-the-badge">
<img src="https://img.shields.io/badge/fsociety-Learning-red?style=for-the-badge">

</p>