# 🌐 SQL Injection Scanner

<p align="center">

<img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/Category-Web%20Security-orange?style=for-the-badge">
<img src="https://img.shields.io/badge/License-MIT-success?style=for-the-badge">
<img src="https://img.shields.io/badge/Status-Experimental-red?style=for-the-badge">

</p>

---

## 📖 About

**SQL Injection Scanner** is a simple Python-based educational tool that performs basic checks for potential SQL Injection vulnerabilities by sending a small set of test payloads to a specified HTTP GET parameter.

This project is intended for learning how automated security testing tools work and should only be used on systems you own or are explicitly authorized to assess.

---

## ✨ Features

- Lightweight Python implementation
- Simple command-line interface
- Tests multiple common SQL Injection payloads
- Detects common SQL-related error messages
- Easy to modify and extend
- Suitable for educational purposes

---

## 📂 Project Structure

```text
sqli-scanner/
│
├── scanner.py
└── README.md
```

---

## ⚙️ Requirements

- Python 3.8+
- requests

Install the required dependency:

```bash
pip install requests
```

---

## 🚀 Usage

Run the scanner from the command line:

```bash
python scanner.py <url> <parameter>
```

### Example

```bash
python scanner.py http://example.local/page id
```

The scanner will send several test inputs to the specified parameter and report whether SQL-related error messages are detected in the response.

---

## 🔍 Detection Method

The scanner:

1. Accepts a target URL and parameter name.
2. Sends several predefined test inputs.
3. Checks the HTTP response for common SQL-related error messages.
4. Reports a potential finding if matching indicators are present.

This is a basic detection approach and should not be considered a complete security assessment.

---

## 📌 Example Output

```text
[*] Target: http://example.local/page
[*] Parameter: id

[!] Potential SQL Injection indicator detected.
```

or

```text
[*] Target: http://example.local/page
[*] Parameter: id

[*] No SQL-related error indicators detected.
```

---

## 📚 Limitations

- Supports only HTTP GET requests.
- Uses a small predefined payload list.
- Relies on SQL-related error messages.
- Does not detect blind SQL Injection.
- Does not perform authenticated testing.
- Does not crawl websites automatically.

---

## 💡 Possible Improvements

- POST request support
- Cookie authentication
- Custom headers
- Automatic parameter discovery
- Blind SQL Injection checks
- Time-based testing
- Boolean-based testing
- HTML report generation
- JSON export
- Colored terminal output
- Multi-threading
- Proxy support

---

## 🛡️ Ethical Use

This tool is designed exclusively for:

- Security education
- Personal laboratory environments
- Capture The Flag (CTF) challenges
- Authorized penetration testing

Do **not** use this software against systems without explicit permission.

---

## ⚠️ Disclaimer

The author assumes no responsibility for misuse of this software.

Users are responsible for ensuring that all testing is performed legally and only on systems they own or are authorized to assess.

---

<p align="center">

### 🛠️ Learn • Test • Improve

<img src="https://img.shields.io/badge/Python-Security-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/Web-Security-red?style=for-the-badge">
<img src="https://img.shields.io/badge/fsociety-Tools-black?style=for-the-badge">

</p>