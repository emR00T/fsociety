# HackTheBox - Crocodile Write-up

## Bilgi
- Platform: HackTheBox Starting Point
- Makine: Crocodile
- Zorluk: Kolay

## Keşif
- nmap: 21/tcp FTP, 80/tcp HTTP

## Sızma
- FTP anonymous login
- allowed.userlist dosyası indirildi
- Kullanıcı adı ve şifreyle web paneline giriş
- Flag alındı

## Öğrenilen
- FTP anonymous erişimi hassas bilgi sızdırır
- Web panellerinde varsayılan kimlikler kullanılmamalı
