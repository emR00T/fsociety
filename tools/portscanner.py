#!/usr/bin/env python3
import socket
import sys

def scan_ports(target, start_port, end_port):
    print(f"\n[*] Hedef: {target}")
    print(f"[*] Port taraniyor: {start_port}-{end_port}\n")
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"[+] Port {port} AÇIK")
        sock.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Kullanım: {sys.argv[0]} <hedef> <başlangıç> <bitiş>")
        sys.exit(1)
    scan_ports(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
