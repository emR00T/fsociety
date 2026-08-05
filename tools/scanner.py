#!/usr/bin/env python3
import socket
import sys
import threading
from datetime import datetime

def scan_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    if sock.connect_ex((target, port)) == 0:
        print(f"[+] Port {port} AÇIK")
    sock.close()

def main():
    if len(sys.argv) != 4:
        print(f"Kullanım: {sys.argv[0]} <hedef> <başlangıç> <bitiş>")
        sys.exit(1)
    
    target = sys.argv[1]
    start = int(sys.argv[2])
    end = int(sys.argv[3])
    
    print(f"\n[*] Tarama başlıyor: {target}")
    print(f"[*] Zaman: {datetime.now()}\n")
    
    threads = []
    for port in range(start, end + 1):
        t = threading.Thread(target=scan_port, args=(target, port))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()
    
    print(f"\n[*] Tarama bitti: {datetime.now()}")

if __name__ == "__main__":
    main()
