# HackTheBox - Dancing Write-up

## Bilgi
- Platform: HackTheBox Starting Point
- Makine: Dancing
- Zorluk: Çok Kolay

## Keşif
- nmap: 135, 139, 445, 5985 açık
- SMB paylaşımları: WorkShares

## Sızma
- smbclient ile WorkShares paylaşımına bağlanıldı
- James.J klasöründe flag.txt bulundu

## Öğrenilen
- SMB null session zafiyeti
- Paylaşım izinleri kontrol edilmeli
