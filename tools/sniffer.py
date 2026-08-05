#!/usr/bin/env python3
from scapy.all import sniff
import sys

def packet_handler(pkt):
    if pkt.haslayer("IP"):
        src = pkt["IP"].src
        dst = pkt["IP"].dst
        proto = pkt["IP"].proto
        print(f"[*] {src} -> {dst} | Proto: {proto} | Len: {len(pkt)}")

def main():
    count = 20
    if len(sys.argv) == 2:
        count = int(sys.argv[1])
    print(f"[*] {count} paket dinleniyor...\n")
    sniff(prn=packet_handler, count=count)

if __name__ == "__main__":
    main()
