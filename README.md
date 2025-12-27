# Öğrenci Yurt Yönetim ve Başvuru Sistemi

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-success)

Bu proje, üniversite yurtlarının yönetim süreçlerini, öğrenci başvurularını, personel yönetimini, ödemeleri ve duyuruları dijital ortamda takip etmek için geliştirilmiş Python tabanlı bir otomasyon sistemidir. Eğitim amaçlı Nesne Yönelimli Programlama dersini kavramak amacıyla hazırlanmıştır.

Veritabanı olarak SQL yerine dosya tabanlı kayıt sistemi (.txt) kullanılarak, temel dosya okuma/yazma ve veri manipülasyonu yetenekleri sergilenmiştir.

## Özellikler ve Modüller

Sistem üç farklı kullanıcı rolüne (Müdür, Öğrenci ve Personel) göre özelleştirilmiş menüler sunar.

### Müdür (Yönetici) Modülü (mudur.py)
Müdür girişi yapıldığında aşağıdaki işlemler gerçekleştirilebilir:
* **Yurt Yönetimi:** Sisteme yeni yurt ekleme, kapasite ve özelliklerini belirleme.
* **Başvuru Takibi:** Öğrencilerin yaptığı yurt başvurularını (basvurular.txt) görüntüleme.
* **Öğrenci Onayı:** Başvuruları onaylayarak öğrencileri yurtlara yerleştirme (yurtlara_kayitli_ogrenciler.txt).
* **Duyuru Paneli:** Tüm öğrencilerin görebileceği duyurular yayınlama (duyurular.txt).
* **Ödeme Kontrolü:** Yapılan ödemeleri ve borç durumlarını listeleme (odemeler.txt).

### Öğrenci Modülü (ogrenci.py)
Öğrenci girişi yapıldığında aşağıdaki işlemler gerçekleştirilebilir:
* **Başvuru:** Mevcut yurtları listeleyip başvuru yapabilme.
* **Ödeme:** Yurt taksit veya ücretlerini ödeme simülasyonu.
* **Duyurular:** Müdür tarafından yayınlanan duyuruları görüntüleme.
* **Profil:** Kendi kayıt durumunu kontrol etme.

### Personel Modülü (personel.py)
Yurt personeli girişi yapıldığında aşağıdaki işlemler gerçekleştirilebilir:
* **İzin Talebi:** Personel, sistem üzerinden izin günü talep edebilir.

### Kimlik Doğrulama (kullanicilar.py)
* Kullanıcı giriş ve kayıt işlemlerini yönetir.
* Kullanıcı verilerini kullanicilar.txt dosyasından doğrulayarak ilgili menüye (Müdür, Öğrenci veya Personel) yönlendirir.

Proje, verileri kalıcı olarak saklamak için metin dosyalarını kullanır.
