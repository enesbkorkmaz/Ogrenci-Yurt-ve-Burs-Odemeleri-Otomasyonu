from base_classes.kullanicilar import Kullanicilar
from genel_islemler import GenelIslemler
import time

#Müdür için alt sınıf. Yurt yönetim yetkilerine sahiptir. Personel ekleyip çıkartabilir. Öğrenci kaydı silebilir. Duyuru ekleyip silebilir. Sisteme yeni yurt ekleyebilir çıkartabilir.
class Mudur(Kullanicilar):
    yurtlar_dosyasi = "yurtlar.txt"

    #Müdür sınıfının constructor metotu
    def __init__(self, kullanici_adi, sifre, isim_soyisim, cinsiyet):
        self.__kullanici_adi = kullanici_adi
        self.__sifre = sifre
        self.__isim_soyisim = isim_soyisim
        self.__cinsiyet = cinsiyet
        self.__kullanicilar = "kullanicilar.txt"
        self.__basvurular = "basvurular.txt"
        self.__duyurular = "duyurular.txt"
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
        self.__sifre = yeni_sifre

    def get_isim_soyisim(self):
        return self.__isim_soyisim
    def set_isim_soyisim(self, yeni_isim_soyisim):
        self.__isim_soyisim = yeni_isim_soyisim

    def get_cinsiyet(self):
        return self.__cinsiyet
    def set_cinsiyet(self, yeni_cinsiyet):
        self.__cinsiyet = yeni_cinsiyet

    def get_duyurular(self):
        return self.__duyurular
    def set_duyurular(self, yeni_dosya):
        self.__duyurular = yeni_dosya

    def get_kullanicilar(self):
        return self.__kullanicilar
    def set_kullanicilar(self, yeni_kullanicilar):
        self.__kullanicilar = yeni_kullanicilar

    def get_basvurular(self):
        return self.__basvurular
    def set_basvurular(self, yeni_basvurular):
        self.__basvurular = yeni_basvurular

    def get_yurtlar(self):
        return self.__yurtlar
    def set_yurtlar(self, yeni_yurtlar_dosyasi):
        self.__yurtlar = yeni_yurtlar_dosyasi

    def get_yurt_kayitlari(self):
        return self.__yurt_kayitlari
    def set_yurt_kayitlari(self, yeni_yurt_kayitlari_dosyasi):
        self.__yurt_kayitlari = yeni_yurt_kayitlari_dosyasi

    def get_odemeler(self):
        return self.__odemeler
    
    def get_yurtlar(self):
        return self.__yurtlar
    def set_yurtlar(self, yeni_yurtlar):
        self.__yurtlar = yeni_yurtlar
    # ---------------------------------------------------------------- Getter ve Setter metotları sonu -------------------------------------------------------
 
    #Yönetici menüsü metodu. Yöneticinin giriş yapması durumunda çalışır. İlgili menülere yönlendirmeler yapılır.
    def menu_goster(self):
        while True:
            GenelIslemler.ekran_temizle()
            print("***** MÜDÜR MENÜSÜ *****".center(120))
            print("1 - Personel Ekle")
            print("2 - Personel Çıkar")
            print("3 - Öğrenci Sil")
            print("4 - Ücretleri Güncelle")
            print("5 - Duyuru Ekle")
            print("6 - Duyuru Sil")
            print("7 - Şifre Değiştir")
            print("8 - Sisteme Yeni Yurt Ekle")
            print("9 - Sistemden Yurt Sil")
            print("0 - Çıkış Yap")
            secim = input("Lütfen bir seçim yapınız: ")

            if secim == "1":
                self.personel_ekle()
            elif secim == "2":
                self.personel_cikarma()
            elif secim == "3":
                self.ogrenci_kayit_sil()
            elif secim == "4":
                self.ucret_guncelle()
            elif secim == "5":
                self.duyuru_ekle()
            elif secim == "6":
                self.duyuru_sil()
            elif secim == "7":
                self.sifre_sifirla()
            elif secim == "8":
                self.yurt_ekle()
            elif secim == "9":
                self.yurt_sil()
            elif secim == "0":
                print("Çıkış yapılıyor...")
                time.sleep(2)
                break
            else:
                print("Geçersiz seçim. Lütfen tekrar deneyin.")
                time.sleep(2)
    
    #Müdür için personel ekle metodu. Personel bilgileri alınır geçerli olup olmadıkları kontrol edilir, geçerliyse kullanicilar.txt dosyasına kaydedilir.
    def personel_ekle(self):
        from.ogrenci import Ogrenci
        GenelIslemler.ekran_temizle()
        print("***** PERSONEL EKLE *****".center(120))
        while True:
            kullanici_adi = input("Kullanıcı adını giriniz: ").strip()
            if Ogrenci.kullanici_adi_kontrol(kullanici_adi, self.get_kullanicilar()):
                print("Bu kullanıcı adı zaten alınmış. Lütfen başka bir kullanıcı adı seçiniz.")
                continue

            sifre = input("Şifrenizi giriniz: ").strip()
            while len(sifre) < 4:
                print("Şifre en az 4 karakter olmalıdır.")
                sifre = input("Şifrenizi tekrar giriniz: ").strip()

            isim_soyisim = input("Ad ve Soyadını giriniz: ").strip()
            eposta = input("E-posta adresinizi giriniz: ").strip()
            if "@" not in eposta or "." not in eposta:
                print("Lütfen geçerli bir e-posta adresi giriniz.")
                continue

            cinsiyet = input("Cinsiyetinizi giriniz (Erkek/Kadın): ").strip()
            yeni_personel = f"personel,{eposta},{kullanici_adi},{sifre},{isim_soyisim},{cinsiyet}"
            GenelIslemler.dosya_ekleme(self.get_kullanicilar(), yeni_personel)
            print("Personel başarıyla eklendi!")
            break

    #Personel silme metodu. Silinmek istenen personelin kullanıcı adı girilir. Kullanıcı adı varsa kullanicilar.txt dosyasından silinir.
    def personel_cikarma(self):
        GenelIslemler.ekran_temizle()
        print("***** PERSONEL ÇIKAR *****".center(120))
        kullanici_adi = input("Çıkarmak istediğiniz personelin kullanıcı adını giriniz: ").strip()
        kullanicilar = GenelIslemler.dosya_okuma(self.get_kullanicilar())
        yeni_kullanicilar = []
        personel_bulundu = False
        for kullanici in kullanicilar:
            if kullanici.startswith("personel") and kullanici.split(",")[2] == kullanici_adi:
                personel_bulundu = True
            else:
                yeni_kullanicilar.append(kullanici)

        if personel_bulundu:
            GenelIslemler.dosya_yazma(self.get_kullanicilar(), yeni_kullanicilar)
            print("Personel çıkarıldı.")
            time.sleep(1.5)
        else:
            print("Bu kullanıcı adıyla bir personel bulunamadı.")
            time.sleep(2)
        
    #Yurt ücretlerinin ve burs ücretinin değişikliğinin yapıldığı metot. Değiştirilmek istenen ücret odemeler.txt dosyasında güncellenir.
    def ucret_guncelle(self):
        GenelIslemler.ekran_temizle()
        print("***** ÜCRET GÜNCELLE *****".center(120))
        odemeler = GenelIslemler.dosya_okuma(self.get_odemeler())
        print("\nMevcut Ücretler:")
        for index, ucret in enumerate(odemeler, start=1):
            tip, miktar = ucret.split(",")
            print(f"{index} - {tip}: {miktar} TL")

        try:
            secim = int(input("\nGüncellemek istediğiniz ücretin numarasını giriniz: ").strip())
            if not (1 <= secim <= len(odemeler)):
                print("Geçersiz seçim. Ana menüye dönülüyor...")
                time.sleep(2)
                return
        except ValueError:
            print("Hatalı giriş! Lütfen sadece sayı giriniz.")
            time.sleep(2)
            return
        
        yeni_miktar = input("Yeni ücret değerini giriniz (TL): ").strip()
        if not yeni_miktar.isdigit() or int(yeni_miktar) <= 0:
            print("Hatalı giriş. Tekrar deneyiniz.")
            time.sleep(2)
            return
        
        eski_veri = odemeler[secim - 1]
        tip = eski_veri.split(",")[0]
        odemeler[secim - 1] = f"{tip},{yeni_miktar}"
        
        GenelIslemler.dosya_yazma(self.get_odemeler(), odemeler)
        print(f"\n{tip} ücreti başarıyla {yeni_miktar} TL olarak güncellendi.")
        time.sleep(2)

    #Öğrenci silmek için metot. Kaydı silinmek istenen öğrencinin kullanıcı adı girilir. Öğrencinin varsa basvurular.txt,yurtlara_kayitli_ogrenciler.txt,kullanicilar.txt dosyalarından kaydı silinir.
    def ogrenci_kayit_sil(self):
        GenelIslemler.ekran_temizle()
        print("***** ÖĞRENCİ KAYDI SİL *****".center(120))
        kullanici_adi = input("Silmek istediğiniz öğrencinin kullanıcı adını giriniz: ").strip()
        kullanicilar = GenelIslemler.dosya_okuma(self.get_kullanicilar())
        yeni_kullanicilar = []
        ogrenci_bulundu = False
        for kullanici in kullanicilar:
            bilgiler = kullanici.split(",")
            if bilgiler[0] == "ogrenci" and bilgiler[2] == kullanici_adi:  
                ogrenci_bulundu = True
            else:
                yeni_kullanicilar.append(kullanici)
        if not ogrenci_bulundu:
            print("Bu kullanıcı adıyla bir öğrenci bulunamadı.")
            time.sleep(2)
            return
        basvurular = GenelIslemler.dosya_okuma(self.get_basvurular())
        yeni_basvurular = []
        for basvuru in basvurular:
            bilgiler = basvuru.split(",")
            if bilgiler[1] != kullanici_adi:  
                yeni_basvurular.append(basvuru)

        yurt_kayitlari = GenelIslemler.dosya_okuma(self.get_yurt_kayitlari())
        yeni_yurt_kayitlari = []

        for kayit in yurt_kayitlari:
            bilgiler = kayit.split(",")
            if bilgiler[0] != kullanici_adi:  
                yeni_yurt_kayitlari.append(kayit)

        GenelIslemler.dosya_yazma(self.get_kullanicilar(), yeni_kullanicilar)
        GenelIslemler.dosya_yazma(self.get_basvurular(), yeni_basvurular)
        GenelIslemler.dosya_yazma(self.get_yurt_kayitlari(), yeni_yurt_kayitlari)

        print("Öğrencinin tüm kaydı başarıyla silindi.")
        time.sleep(2)

    #Duyuru ekleme metodu. Müdür öğrencilerin ve personelin bilgilenmesi için duyuru ekleyebilir. 
    def duyuru_ekle(self):
        GenelIslemler.ekran_temizle()
        print("***** DUYURU EKLE *****")
        duyuru_metni = input("Duyuru metnini giriniz: ").strip()
        yeni_duyuru = f"duyuru,{duyuru_metni}"
        GenelIslemler.dosya_ekleme("duyurular.txt", yeni_duyuru)
        print("Duyuru başarıyla eklendi!")

    # Duyuru silme metodu. Müdür geçersiz kalmış silinmesi gereken duyuruları seçip silebilir.
    def duyuru_sil(self):
        GenelIslemler.ekran_temizle()
        print("***** DUYURU SİL *****".center(120))
        duyurular = GenelIslemler.dosya_okuma("duyurular.txt")
        for index, duyuru in enumerate(duyurular, start=1):
            print(f"{index}. {duyuru.split(',')[1]}")  
        duyuru_index = int(input("Silmek istediğiniz duyurunun numarasını giriniz: ").strip())

        if 0 < duyuru_index <= len(duyurular):
            duyurular.pop(duyuru_index - 1)
            GenelIslemler.dosya_yazma("duyurular.txt", duyurular)
            print("Duyuru başarıyla silindi.")
        else:
            print("Geçersiz duyuru numarası.")

    #POLYMORFİZM Müdür sınıfı için şifre sıfırlama metodu. 
    def sifre_sifirla(self):
        GenelIslemler.ekran_temizle()
        print("***** MÜDÜR ŞİFRE SIFIRLAMA *****".center(120))
        while True:
            yeni_sifre = input("Yeni şifrenizi giriniz (en az 4 karakter): ").strip()
            if len(yeni_sifre) < 4:
                print("Şifre en az 4 karakterden oluşmalıdır.")
                continue

            yeni_sifre_tekrar = input("Yeni şifrenizi tekrar giriniz: ").strip()
            if yeni_sifre != yeni_sifre_tekrar:
                print("Şifreler uyuşmuyor. Lütfen tekrar deneyiniz.")
                continue
            
            mevcut_kullanicilar = GenelIslemler.dosya_okuma(self.get_kullanicilar())
            for index, kullanici in enumerate(mevcut_kullanicilar):
                bilgiler = kullanici.split(",")
                if bilgiler[0] == "mudur" and bilgiler[2] == self.get_kullanici_adi():
                    bilgiler[3] = yeni_sifre 
                    mevcut_kullanicilar[index] = ",".join(bilgiler)
                    GenelIslemler.dosya_yazma(self.get_kullanicilar(), mevcut_kullanicilar)
                    print("Şifreniz başarıyla güncellendi.")
                    return

    #Toplam yurt sayısını tarayan class metodu. yurtlar.txt dosyasından çekilen nesneler taranır. Toplam çıktısı verilir.
    @classmethod
    def toplam_yurt_sayisi(cls):
        yurt_sayisi = 0
        yurtlar = GenelIslemler.dosya_okuma(cls.yurtlar_dosyasi) 
        for yurt in yurtlar:
            if yurt.startswith("yurt"):  
                yurt_sayisi += 1
        return f"Sistemde kayıtlı toplam yurt sayısı: {yurt_sayisi}"

    #Yurt ekleme metodu. Müdür sisteme yeni yurt kaydı yapabilir. Yeni yurtlar yurtlar.txt dosyasına kaydedilir.
    def yurt_ekle(self):
        GenelIslemler.ekran_temizle()
        print("***** YENİ YURT EKLE *****".center(120))
        cinsiyet = input("Yurdun cinsiyetini giriniz (Erkek/Kadın): ").strip().capitalize()
        if cinsiyet not in ["Erkek", "Kadın"]:
            print("Geçersiz giriş!")
            time.sleep(2)
            return

        sehir = input("Yurdun bulunduğu şehri giriniz: ").strip().upper()
        yurt_adi = input("Yurdun adını giriniz: ").strip()
        toplam_kapasite = input("Yurdun toplam kapasitesini giriniz: ").strip()
        tip = input("Yurdun tipini giriniz (tip1, tip2, ..., tip6): ").strip().lower()

        if not toplam_kapasite.isdigit() or int(toplam_kapasite) <= 0:
            print("Lütfen geçerli bir değer giriniz")
            time.sleep(2)
            return
        if tip not in ["tip1", "tip2", "tip3", "tip4", "tip5", "tip6"]:
            print("Lütfen geçerli bir tip giriniz.")
            time.sleep(2)
            return

        yeni_yurt = f"yurt,{cinsiyet},{sehir},{yurt_adi},{toplam_kapasite},{toplam_kapasite},{tip}"
        yurtlar = GenelIslemler.dosya_okuma(self.get_yurtlar())
        yurtlar.append(yeni_yurt)
        GenelIslemler.dosya_yazma(self.get_yurtlar(), yurtlar)
        print("Yeni yurt başarıyla eklendi!")
        time.sleep(2)
        print(Mudur.toplam_yurt_sayisi())
        time.sleep(2)

    #Yurt bilgisini listeleyen statik metot. Diğer classlarda da kullanılabilir.
    @staticmethod
    def yurt_bilgisi_goster(yurtlar_dosyasi):
        yurtlar = GenelIslemler.dosya_okuma(yurtlar_dosyasi)
        if not yurtlar:
            print("Yurt bilgisi bulunamadı.")
            return

        print("***** YURT BİLGİLERİ *****".center(120))
        for index, yurt in enumerate(yurtlar, start=1):
            bilgiler = yurt.split(",")
            yurt_adi = bilgiler[3]
            kapasite = bilgiler[4]
            bos_kontenjan = bilgiler[5]
            tip = bilgiler[6]
            print(f"{index} - {yurt_adi} | Kapasite: {kapasite} | Boş Kontenjan: {bos_kontenjan} | Tip: {tip}")

    #Yurt silme metodu. Müdür silinmek istenen yurdu girerek yurtlar.txt dosyasından silebilir.
    def yurt_sil(self):
        GenelIslemler.ekran_temizle()
        print("***** YURT SİL *****".center(120))
        print("Mevcut yurtlar:")
        Mudur.yurt_bilgisi_goster(self.get_yurtlar()) 
        yurt_adi = input("Silmek istediğiniz yurdun adını giriniz: ").strip()

        yurtlar = GenelIslemler.dosya_okuma(self.get_yurtlar())
        yeni_yurtlar = []
        yurt_bulundu = False
        for yurt in yurtlar:
            bilgiler = yurt.split(",")
            if bilgiler[3] == yurt_adi:
                yurt_bulundu = True
            else:
                yeni_yurtlar.append(yurt)
        if yurt_bulundu:
            GenelIslemler.dosya_yazma(self.get_yurtlar(), yeni_yurtlar)
            print("Yurt başarıyla silindi!")
        else:
            print("Belirtilen yurt bulunamadı.")
        time.sleep(2)
