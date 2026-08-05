# HackTheBox - Redeemer Write-up

## Bilgi
- Platform: HackTheBox Starting Point
- Makine: Redeemer
- Zorluk: Çok Kolay

## Keşif
- nmap: 6379/tcp Redis açık

## Sızma
- redis-cli ile bağlanıldı
- KEYS * ile anahtarlar listelendi
- GET flag ile flag alındı

## Öğrenilen
- Redis varsayılan olarak şifresiz çalışır
- İnternete açık Redis sunucuları büyük risk
- Her zaman kimlik doğrulama eklenmeli
