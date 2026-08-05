# HackTheBox - Appointment Write-up

## Bilgi
- Platform: HackTheBox Starting Point
- Makine: Appointment
- Zorluk: Çok Kolay

## Keşif
- nmap: 80/tcp HTTP (Apache)

## Sızma
- Login sayfasında SQL Injection
- Kullanıcı adı: admin'#
- Şifre: boş
- Başarılı giriş, flag görüntülendi

## Öğrenilen
- SQL Injection hala en yaygın web zafiyetlerinden
- Kullanıcı girdileri asla doğrudan sorguya eklenmemeli
- Prepared statement kullanılmalı
