from base_classes.kullanicilar import Kullanicilar
from genel_islemler import GenelIslemler
import time

#Öğrenciler için alt sınıf. Öğrenci kayıt olabilir. Burs ve yurt başvuruları yapabilir. Yurt ücretini ödeyebilir.
class Ogrenci(Kullanicilar):
    kullanicilar = "kullanicilar.txt"
    #Öğrenci sınıfının constructor metotu.
    def __init__(self, kullanici_adi, sifre, isim_soyisim, bakiye,cinsiyet):
        self.__kullanici_adi = kullanici_adi
        self.__sifre = sifre
        self.__isim_soyisim = isim_soyisim
        self.__bakiye = bakiye
        self.__cinsiyet = cinsiyet
        self.__kullanicilar = "kullanicilar.txt"
        self.__basvurular = "basvurular.txt"
        self.__yurt_kayitlari = "yurtlara_kayitli_ogrenciler.txt"
        self.__odemeler = "odemeler.txt"
        self.__yurtlar = "yurtlar.txt"
    
    # ---------------------------------------------------------------- Getter ve Setter metotları ---------------------------------------------------------
    def get_kullanici_adi(self):
        return self.__kullanici_adi

    def set_kullanici_adi(self, yeni_kullanici_adi):
        self.__kullanici_adi = yeni_kullanici_adi

    def get_sifre(self):
        return self.__sifre

    def set_sifre(self, yeni_sifre):
        if len(yeni_sifre) < 4:
            print("Şifre en az 4 karakter olmalıdır.")
        else:
            self.__sifre = yeni_sifre

    def get_isim_soyisim(self):
        return self.__isim_soyisim

    def set_isim_soyisim(self, yeni_isim_soyisim):
        self.__isim_soyisim = yeni_isim_soyisim

    def get_bakiye(self):
        return self.__bakiye

    def set_bakiye(self, yeni_bakiye):
        if yeni_bakiye < 0:
            print("Bakiye negatif olamaz.")
        else:
            self.__bakiye = yeni_bakiye

    def get_cinsiyet(self):
        return self.__cinsiyet

    def set_cinsiyet(self, yeni_cinsiyet):
        self.__cinsiyet = yeni_cinsiyet
        
    def get_kullanicilar(self):
        return self.__kullanicilar

    def set_kullanicilar_dosyasi(self, yeni_dosya):
        self.__kullanicilar = yeni_dosya

    def get_basvurular(self):
        return self.__basvurular

    def set_basvurular(self, yeni_dosya):
        self.__basvurular = yeni_dosya

    def get_yurt_kayitlari(self):
        return self.__yurt_kayitlari

    def set_yurt_kayitlari(self, yeni_yurt_kayitlari_dosyasi):
        self.__yurt_kayitlari = yeni_yurt_kayitlari_dosyasi

    def get_odemeler(self):
        return "odemeler.txt"

    def get_yurt_ucreti(self, yurt_tipi):
        ucretler = self.get_odemeler()
        for ucret in ucretler:
            ucret_bilgisi = ucret.split(",")
            if ucret_bilgisi[0] == yurt_tipi:
                return int(ucret_bilgisi[1])  
        return None 
    
    def get_yurtlar(self):
        return self.__yurtlar
    
    def set_yurtlar(self, yeni_dosya):
        self.__yurtlar = yeni_dosya

    # ---------------------------------------------------------------- Getter ve Setter metotları sonu -------------------------------------------------------

    #Toplam öğrenci sayısını döndüren class metotu. Toplam öğrenci taranır, çıktısı verilir.
    @classmethod
    def toplam_ogrenci_sayisi(cls):
        ogrenci_sayisi = 0
        kullanicilar = GenelIslemler.dosya_okuma(cls.kullanicilar)  # Dosyayı oku
        for kullanici in kullanicilar:
            if kullanici.startswith("ogrenci"):
                ogrenci_sayisi += 1  

        return f"{ogrenci_sayisi}"

    #POLYMORFİZM. Öğrenci sınıfının kendi menüsünü gösterir. Öğrencinin başvuru ve yurt durumuna göre seçenekler değişir.
    def menu_goster(self):
        burs_basvurusu_var = False
        yurt_basvurusu_var = False
        yurtta_kaliyor_mu = False
        basvurular = GenelIslemler.dosya_okuma("basvurular.txt")
        for basvuru in basvurular:
            bilgiler = basvuru.split(",")
            if bilgiler[0] == "burs" and bilgiler[1] == self.get_kullanici_adi():
                burs_basvurusu_var = True
            elif bilgiler[0] == "yurt" and bilgiler[1] == self.get_kullanici_adi() and bilgiler[-1] == "beklemede":
                yurt_basvurusu_var = True
            elif bilgiler[0] == "yurt" and bilgiler[1] == self.get_kullanici_adi() and bilgiler[-1] == "onaylandı":
                yurtta_kaliyor_mu = True
        
        while True:
            print("***** ÖĞRENCİ MENÜSÜ *****".center(120))
            print(f"Merhaba {self.get_isim_soyisim()}, ")
            print(f"Mevcut Bakiyeniz: {self.get_bakiye()} TL")
            print(f"***Toplam Öğrenci Sayısı: {Ogrenci.toplam_ogrenci_sayisi()}***\n")
            print(f"1 - Burs Başvurusu Yap {'(Başvuruldu)' if burs_basvurusu_var else ''}")
            if yurtta_kaliyor_mu:
                print("2 - Yurt Ücretini Öde")
            else:
                print(f"2 - Yurt Başvurusu Yap {'(Başvuruldu)' if yurt_basvurusu_var else ''}")

            print("3 - Başvuru Durumunu Görüntüle")
            print("4 - Şifre Değiştir")
            print("5 - Çıkış Yap")
            
            secim = input("Lütfen bir seçim yapınız: ").strip()

            if secim == "1":
                if burs_basvurusu_var:
                    print("Zaten burs başvurusu yaptınız. Tekrar başvuramazsınız.")
                else:
                    self.burs_basvurusu_yap()
            elif secim == "2":
                if yurtta_kaliyor_mu:
                    self.yurt_ucreti_ode() 
                elif yurt_basvurusu_var:
                    print("Zaten yurt başvurusu yaptınız. Tekrar başvuramazsınız.")
                    time.sleep(2)
                    GenelIslemler.ekran_temizle()
                else:
                    self.yurt_basvurusu_yap()
            elif secim == "3":
                self.basvuru_durumunu_goruntule()
            elif secim == "4":
                GenelIslemler.ekran_temizle()
                self.sifre_sifirla()
            elif secim == "5":
                print("Çıkış yapılıyor...")
                time.sleep(2)
                break
            else:
                print("Geçersiz seçim. Lütfen tekrar deneyin.")
                time.sleep(2)
                GenelIslemler.ekran_temizle()

    #Öğrenci başvuru yaptıysa başvuru durumu basvurular.txt dosyasından kontrol edilir. Öğrenci durumu hakkında bilgilendirilir.              
    def basvuru_durumunu_goruntule(self):
        GenelIslemler.ekran_temizle()
        print("***** BAŞVURU DURUMU *****".center(120))
        burs_durumu = "Henüz başvurulmamış."
        yurt_durumu = "Henüz başvurulmamış."
        basvurular = GenelIslemler.dosya_okuma("basvurular.txt")
        for basvuru in basvurular:
            bilgiler = basvuru.split(",")
            if bilgiler[0] == "burs" and bilgiler[1] == self.get_kullanici_adi():
                if bilgiler[-1] == "beklemede":
                    burs_durumu = f"Başvurunuz bekleme aşamasında."
                elif bilgiler[-1] == "reddedildi":
                    burs_durumu = "Üzgünüz burs almaya hak kazanamadınız."
                else:
                    burs_durumu = "Tebrikler burs kazandınız."
            elif bilgiler[0] == "yurt" and bilgiler[1] == self.get_kullanici_adi():
                if bilgiler[-1] == "beklemede":
                  yurt_durumu = "Başvurunuz bekleme aşamasında."
                elif bilgiler[-1] == "reddedildi":
                    yurt_durumu = "Üzgünüz yurt kontenjanı dolu veya şartları karşılamıyorsunuz. Başvurunuz reddedildi."
                else:
                    yurt_durumu = f"Tebrikler yurt kazandınız."
                    
        print(f"Burs başvuru durumu: {burs_durumu}")
        print(f"Yurt başvuru durumu: {yurt_durumu}")
        input("Geri dönmek için \"enter\" tuşuna basın.")
        GenelIslemler.ekran_temizle()
    
    #POLYMORFİZM. Öğrenci sınıfı için şifre sıfırlama metotu.
    def sifre_sifirla(self):
        print("***** ÖĞRENCİ ŞİFRE SIFIRLAMA *****".center(120))
        while True:
            yeni_sifre = input("Yeni şifrenizi giriniz (en az 4 karakter): ")
            if len(yeni_sifre) < 4:
                print("Lütfen 4 karakterden daha uzun bir şifre giriniz.")
                continue

            yeni_sifre_dogrulama = input("Yeni şifrenizi tekrar giriniz: ")
            if yeni_sifre != yeni_sifre_dogrulama:
                print("Şifreler uyuşmuyor. Lütfen tekrar deneyiniz.")
                continue
            break

        kullanicilar = GenelIslemler.dosya_okuma(self.get_kullanicilar())
        for index, kullanici in enumerate(kullanicilar):
            bilgiler = kullanici.split(',')
            if bilgiler[2] == self.get_kullanici_adi():
                bilgiler[3] = yeni_sifre
                kullanicilar[index] = ','.join(bilgiler)
                break

        GenelIslemler.dosya_yazma(self.get_kullanicilar(), kullanicilar)
        self.set_sifre(yeni_sifre)
        print("Öğrenci şifresi başarıyla güncellendi.")
        time.sleep(2)
        GenelIslemler.ekran_temizle()

    #Burs başvurusu metotu. Öğrenci bilgilerini girerek başvuru yapabilir. Başvurular basvurular.txt dosyasına kaydedilir.
    def burs_basvurusu_yap(self):
        GenelIslemler.ekran_temizle()
        print("***** BURS BAŞVURUSU *****".center(120))
        yas = input("Yaşınızı giriniz: ").strip()
        aile_gelir = input("Ailenizin yıllık gelirini giriniz: ").strip()
        yks_puani = input("YKS puanınızı giriniz: ").strip()

        if not yas.isdigit() or not aile_gelir.isdigit() or not yks_puani.isdigit():
            print("Geçersiz biçim.Sayısal değerler kullanın. ")
            time.sleep(2)
            GenelIslemler.ekran_temizle()
            return
        if int(yks_puani) >560 or int(yks_puani) < 0:
            print("Geçersiz puan. Tekrar deneyin.")
            time.sleep(2)
            GenelIslemler.ekran_temizle()
            return

        basvuru_bilgisi = f"burs,{self.get_kullanici_adi()},{self.get_isim_soyisim()},{yas},{aile_gelir},{yks_puani},beklemede"
        GenelIslemler.dosya_ekleme("basvurular.txt", basvuru_bilgisi)
        print("Burs başvurusu başarıyla yapıldı.")
        time.sleep(2)
        GenelIslemler.ekran_temizle()

    #Burs başvurusu metotu. Öğrenci bilgilerini girerek başvuru yapabilir. Başvurular basvurular.txt dosyasına kaydedilir.
    def yurt_basvurusu_yap(self):
        GenelIslemler.ekran_temizle()
        print("***** YURT BAŞVURUSU *****".center(120))
        yas = input("Yaşınızı giriniz: ").strip()
        aile_gelir = input("Ailenizin yıllık gelirini giriniz: ").strip()
        ikamet_sehir = input("İkamet ettiğiniz şehri giriniz: ").strip()
        basvurulan_sehir = input("Başvurmak istediğiniz şehri giriniz: ").strip()

        if not yas.isdigit() or not aile_gelir.isdigit():
            print("Geçersiz biçim.Sayısal değerler kullanın.")
            return

        basvuru_bilgisi = f"yurt,{self.get_kullanici_adi()},{self.get_isim_soyisim()},{yas},{aile_gelir},{ikamet_sehir},{basvurulan_sehir},{self.get_cinsiyet()},beklemede"
        GenelIslemler.dosya_ekleme("basvurular.txt", basvuru_bilgisi)
        print("Yurt başvurusu başarıyla yapıldı!")
        time.sleep(2)
        GenelIslemler.ekran_temizle()

    #Yurt ücreti ödeme metotu. Öğrenciler yurtta kalıyorsa ilgili yurdun ücreti odemeler.txt dosyasından okunur. Öğrencinin de bakiyesi yetiyorsa bu ücret bakiyeden düşülür. kullanicilar.txt dosyasında yurt ücreti ödendi olarak güncellenir.
    def yurt_ucreti_ode(self):
        GenelIslemler.ekran_temizle()
        print("***** YURT ÜCRETİ ÖDE *****".center(120))
        yurt_kayitlari = GenelIslemler.dosya_okuma(self.get_yurt_kayitlari())
        ogrenci_bulundu = False
        yurt_adı = ""

        for index, kayit in enumerate(yurt_kayitlari):
            bilgiler = kayit.split(",")
            if bilgiler[0] == self.get_kullanici_adi(): 
                ogrenci_bulundu = True
                yurt_adı = bilgiler[1]
                if bilgiler[-1] == "ödendi":
                    print("Yurt ücreti zaten ödendi. Geri dönülüyor...")
                    time.sleep(2)
                    GenelIslemler.ekran_temizle()
                    return
                break

        if not ogrenci_bulundu:
            print("Öğrenci kaydı bulunamadı. Lütfen tekrar deneyin.")
            time.sleep(2)
            GenelIslemler.ekran_temizle()
            return

        yurt_tipi = ""
        yurtlar = GenelIslemler.dosya_okuma(self.get_yurtlar()) 
        for yurt in yurtlar:
            yurt_bilgisi = yurt.split(",")
            if yurt_bilgisi[3] == yurt_adı:  
                yurt_tipi = yurt_bilgisi[-1]  
                break
        
        yurt_ucreti = 0
        ucretler = GenelIslemler.dosya_okuma(self.get_odemeler())
        for ucret in ucretler:
            tip, miktar = ucret.split(",")
            if tip == yurt_tipi:
                yurt_ucreti = int(miktar)
                break

        print(f"{yurt_adı} Yurt Ücreti: {yurt_ucreti} TL")
        onay = input("Ödemeyi onaylıyor musunuz? (E/H): ").strip().lower()
        if onay == "e":
            kullanicilar = GenelIslemler.dosya_okuma(self.get_kullanicilar())
            for index, kullanici in enumerate(kullanicilar):
                bilgiler = kullanici.split(',')
                if bilgiler[2] == self.get_kullanici_adi():
                    mevcut_bakiye = int(bilgiler[5])
                    if mevcut_bakiye >= yurt_ucreti:
                        yeni_bakiye = mevcut_bakiye - yurt_ucreti
                        self.set_bakiye(yeni_bakiye)
                        bilgiler[5] = str(yeni_bakiye)
                        kullanicilar[index] = ','.join(bilgiler)

                        for i, kayit in enumerate(yurt_kayitlari):
                            if kayit.startswith(self.get_kullanici_adi()):
                                yurt_kayitlari[i] = f"{self.get_kullanici_adi()},{yurt_adı},ödendi"
                                break

                        GenelIslemler.dosya_yazma(self.get_kullanicilar(), kullanicilar)
                        GenelIslemler.dosya_yazma(self.get_yurt_kayitlari(), yurt_kayitlari)
                        print("Yurt ücreti başarıyla ödendi.")
                        time.sleep(2)
                        GenelIslemler.ekran_temizle()
                        return
                    else:
                        print("Yetersiz bakiye! Lütfen personelden bakiye yükleyiniz.")
                        time.sleep(2)
                        GenelIslemler.ekran_temizle()
                        return
        elif onay == "h":
            print("Ödeme işlemi iptal edildi.")
            time.sleep(2)
            GenelIslemler.ekran_temizle()
            return
        else:
            print("Geçersiz yanıt.")
            time.sleep(2)
            GenelIslemler.ekran_temizle()

    #kullanıcı adı kontrolü için statik metot. Diğer classlarda da kullanılabilir. Sistemde belirtilen kullanıcı adı var mı yok mu diye kontrol eder.
    @staticmethod
    def kullanici_adi_kontrol(kullanici_adi, kullanicilar_dosyasi):
        kullanicilar = GenelIslemler.dosya_okuma(kullanicilar_dosyasi)
        for kullanici in kullanicilar:
            bilgiler = kullanici.split(",")
            if bilgiler[2] == kullanici_adi: 
                return True  
        return False    
        