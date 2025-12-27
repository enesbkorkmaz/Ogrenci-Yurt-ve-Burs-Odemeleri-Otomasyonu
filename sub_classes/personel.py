from base_classes.kullanicilar import Kullanicilar
from genel_islemler import GenelIslemler
import time

#Personeller için alt sınıf. Personel başvuruları onaylayabilir,reddedebilir. Öğrencilere bakiye yükleyebilir. Burs ödemelerini yapabilir. Yurt ödenme durumunu sıfırlayabilir.
class Personel(Kullanicilar):
    kullanicilar = "kullanicilar.txt"
    #Personel sınıfı constructor metotu.
    def __init__(self, kullanici_adi, sifre, isim_soyisim, cinsiyet):
        self.__kullanici_adi = kullanici_adi 
        self.__sifre = sifre  
        self.__isim_soyisim = isim_soyisim 
        self.__cinsiyet = cinsiyet
        self.__kullanicilar = "kullanicilar.txt"
        self.__basvurular = "basvurular.txt"
        self.__odemeler = "odemeler.txt"
        self.__yurtlar = "yurtlar.txt"
        self.__yurt_kayitlari = "yurtlara_kayitli_ogrenciler.txt"
        
    #-------------------------------------------------------------------Getter ve Setter metotları---------------------------------------------------------

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

    def get_cinsiyet(self):
        return self.__cinsiyet

    def set_cinsiyet(self, yeni_cinsiyet):
        self.__cinsiyet = yeni_cinsiyet

    def get_kullanicilar(self):
        return self.__kullanicilar

    def set_kullanicilar(self, yeni_dosya):
        self.__kullanicilar = yeni_dosya

    def get_basvurular(self):
        return self.__basvurular

    def set_basvurular(self, yeni_dosya):
        self.__basvurular = yeni_dosya

    def get_odemeler(self):
        return self.__odemeler

    def set_odemeler(self, yeni_dosya):
        self.__odemeler = yeni_dosya

    def get_yurtlar(self):
        return self.__yurtlar

    def set_yurtlar(self, yeni_yurtlar_dosyasi):
        self.__yurtlar = yeni_yurtlar_dosyasi

    def get_yurt_kayitlari(self):
        return self.__yurt_kayitlari

    def set_yurt_kayitlari(self, yeni_yurt_kayitlari_dosyasi):
        self.__yurt_kayitlari = yeni_yurt_kayitlari_dosyasi

    #-----------------------------------------------------------------Getter ve Setter metotları sonu-------------------------------------------------------
    #POLYMORFİZM. Personel için menü göster metotu. Personelin giriş yapması durumunda kendi menüsünü gösterir.
    def menu_goster(self):
        while True:
            print("***** PERSONEL MENÜSÜ *****".center(120))
            print(f"***{Personel.toplam_personel_sayisi()}***\n")
            print("1 - Burs Başvurularını Görüntüle")
            print("2 - Yurt Başvurularını Görüntüle")
            print("3 - Öğrenci Bakiye Yükle")
            print("4 - Burs Ödemesi Yap")
            print("5 - Yurt Ödenme Durumunu Sıfırla")
            print("6 - Ana Menüye Dön")
            secim = input("Lütfen bir seçim yapınız: ")

            if secim == "1":
                self.burs_basvurularini_goruntule()
            elif secim == "2":
                print("Yurt kontenjanları güncelleniyor. Lütfen bekleyin...")
                time.sleep(3)
                self.yurt_kontenjan_guncelle()
                time.sleep(1)
                self.yurt_basvurularini_goruntule()

            elif secim == "3":
                self.bakiye_yukle()
            elif secim == "4":
                self.burs_odeme_yap()
            elif secim == "5":
                self.odemeleri_sifirla()
            elif secim == "6":
                print("Ana menüye dönülüyor.")
                break
            else:
                print("Geçersiz seçim. Lütfen tekrar deneyin.")
                time.sleep(1)
                GenelIslemler.ekran_temizle()

    #Yurt kontenjanlarını otomatik güncelleyen metot.  yurtta_kalan_ogrenciler.txt dosyasındaki öğrencilerin sayısı hesaplanır, yurtlar.txt dosyasından bu sayı düşülür ve dosya güncellenir.
    def yurt_kontenjan_guncelle(self):
        yurtlar = GenelIslemler.dosya_okuma(self.get_yurtlar())
        yurt_kayitlari = GenelIslemler.dosya_okuma(self.get_yurt_kayitlari())
        yeni_yurt_listesi = []
        for yurt in yurtlar:
            yurt_bilgisi = yurt.split(",")
            yurt_adi = yurt_bilgisi[3]  
            toplam_kapasite = int(yurt_bilgisi[4])  
            kayitli_ogrenci_sayisi = 0
            for kayit in yurt_kayitlari:
                if yurt_adi in kayit:
                    kayitli_ogrenci_sayisi += 1

            bos_kapasite = toplam_kapasite - kayitli_ogrenci_sayisi
            if bos_kapasite < 0:
                bos_kapasite = 0 

            yurt_bilgisi[5] = str(bos_kapasite)
            yeni_yurt_listesi.append(",".join(yurt_bilgisi))
        GenelIslemler.dosya_yazma(self.get_yurtlar(), yeni_yurt_listesi)
        print("Yurt kontenjan bilgileri başarıyla güncellendi!")

    #Yurt başvurularını listeleyen metot. Personel başvurular arasından seçim yapıp onaylayabilir, reddedebilir. Onaylanacak öğrenciye uygun yurt veya yurtlar listelenir.
    def yurt_basvurularini_goruntule(self):
        GenelIslemler.ekran_temizle()
        print("***** YURT BAŞVURULARI *****".center(120))
        basvurular = GenelIslemler.dosya_okuma(self.get_basvurular())
        bekleyen_basvurular = [basvuru for basvuru in basvurular if "yurt" in basvuru and basvuru.split(",")[-1] == "beklemede"]

        if not bekleyen_basvurular:
            print("Bekleyen yurt başvurusu bulunmamaktadır.")
            input("Geri dönmek için \"Enter\" tuşuna basınız...")
            GenelIslemler.ekran_temizle()
            return

        for index, basvuru in enumerate(bekleyen_basvurular, start=1):
            bilgiler = basvuru.split(",")
            print(f"{index} - {bilgiler[1]} | {bilgiler[2]} | Yaş: {bilgiler[3]} | Şehir: {bilgiler[6]} | Cinsiyet: {bilgiler[7]}")

        print("1 - Öğrenciyi Yerleştir")
        print("2 - Başvuruyu Reddet")
        print("3 - Geri Dön")
        secim = input("Seçiminiz: ").strip()

        if secim == "1":
            basvuru_index = int(input("Yerleştirmek istediğiniz öğrencinin numarasını giriniz: ").strip()) - 1
            if 0 <= basvuru_index < len(bekleyen_basvurular):
                secilen_basvuru = bekleyen_basvurular[basvuru_index]
                bilgiler = secilen_basvuru.split(",")

                kullanici_adi = bilgiler[1]
                isim_soyisim = bilgiler[2]
                cinsiyet = bilgiler[7]
                tercih_sehri = bilgiler[6]

                yurtlar = GenelIslemler.dosya_okuma(self.get_yurtlar())
                uygun_yurtlar = []
                for yurt in yurtlar:
                    yurt_bilgileri = yurt.split(",")
                    if yurt_bilgileri[1].lower() == cinsiyet.lower() and yurt_bilgileri[2].lower() == tercih_sehri.lower():
                        uygun_yurtlar.append(yurt)

                if not uygun_yurtlar:
                    print("Seçilen şehre ve cinsiyete uygun yurt bulunamadı.")
                    time.sleep(1)
                    print("Geri dönülüyor...")
                    time.sleep(2)
                    GenelIslemler.ekran_temizle()
                    return
                GenelIslemler.ekran_temizle()
                print("***** UYGUN YURTLAR *****".center(120))
                for i, yurt in enumerate(uygun_yurtlar, start=1):
                    yurt_bilgileri = yurt.split(",")
                    print(f"{i} - {yurt_bilgileri[3]} | Kapasite: {yurt_bilgileri[4]} | Boş Kontenjan: {yurt_bilgileri[5]}")

                yurt_secim = int(input("Öğrenciyi yerleştirmek istediğiniz yurdun numarasını giriniz: ").strip()) - 1

                if 0 <= yurt_secim < len(uygun_yurtlar):
                    secilen_yurt = uygun_yurtlar[yurt_secim]
                    yurt_bilgileri = secilen_yurt.split(",")
                    yurt_adi = yurt_bilgileri[3]

                    yeni_kayit = f"{kullanici_adi},{yurt_adi},ödenmedi"
                    GenelIslemler.dosya_ekleme("yurtlara_kayitli_ogrenciler.txt", yeni_kayit)

                    for i, basvuru in enumerate(basvurular):
                        if basvuru == secilen_basvuru:
                            basvurular[i] = secilen_basvuru.replace("beklemede", "onaylandı")
                            break

                    GenelIslemler.dosya_yazma(self.get_basvurular(), basvurular)
                    print(f"{isim_soyisim} öğrencisi '{yurt_adi}' yurduna başarıyla yerleştirildi!")
                    self.yurt_kontenjan_guncelle()
                    input("Devam etmek için 'Enter' tuşuna basınız...")
                    GenelIslemler.ekran_temizle()
                else:
                    print("Geçersiz yurt seçimi.")
                    time.sleep(1)
                    GenelIslemler.ekran_temizle()
            else:
                print("Geçersiz öğrenci seçimi.")
                time.sleep(1)
                GenelIslemler.ekran_temizle()
        elif secim == "2":
            basvuru_index = int(input("Reddetmek istediğiniz öğrencinin numarasını giriniz: ").strip()) - 1
            if 0 <= basvuru_index < len(bekleyen_basvurular):
                secilen_basvuru = bekleyen_basvurular[basvuru_index]
                for i, basvuru in enumerate(basvurular):
                    if basvuru == secilen_basvuru:
                        basvurular[i] = secilen_basvuru.replace("beklemede", "reddedildi")
                        break

                GenelIslemler.dosya_yazma(self.get_basvurular(), basvurular)
                print("Başvuru başarıyla reddedildi.")
                input("Devam etmek için 'Enter' tuşuna basınız...")
                GenelIslemler.ekran_temizle()
            else:
                print("Geçersiz seçim.")
        elif secim == "3":
            print("Bir önceki menüye dönülüyor...")
            time.sleep(2)
            GenelIslemler.ekran_temizle()
        else:
            print("Geçersiz seçim, lütfen tekrar deneyiniz.")
            time.sleep(2)
            GenelIslemler.ekran_temizle()

    #Burs başvurularını listeleyen metot. Personel onaylayabilir veya reddedebilir.
    def burs_basvurularini_goruntule(self):
        GenelIslemler.ekran_temizle()
        basvurular = GenelIslemler.dosya_okuma(self.get_basvurular())
        print("***** BURS BAŞVURULARI *****".center(120))
        beklemede_burslar = []
        for index, basvuru in enumerate(basvurular):
            bilgiler = basvuru.split(",")
            if bilgiler[0] == "burs" and bilgiler[-1] == "beklemede":
                beklemede_burslar.append((index + 1, bilgiler))

        if not beklemede_burslar:
            print("Henüz beklemede burs başvurusu yok.")
            time.sleep(2)
            GenelIslemler.ekran_temizle()
            return

        print("Beklemede olan burs başvuruları: ")
        for numara, bilgiler in beklemede_burslar:
            print(f"{numara}. Kullanıcı Adı: {bilgiler[1]}, İsim Soyisim: {bilgiler[2]}, Yaş: {bilgiler[3]},Yıllık Gelir: {bilgiler[4]},YKS Puanı:{bilgiler[5]}")
        print("1 - Onayla")
        print("2 - Reddet")
        print("3 - Geri dön")
        secim = input("Lütfen bir seçim yapınız: ")
        
        if secim == "1":
            self.burs_basvuru_onayla()
        elif secim == "2":
            self.burs_basvuru_reddet()
        elif secim == "3":
            return
        else:
            print("Geçersiz seçim.")

    #Burs başvurusu onaylanacak öğrencinin basvurular.txt dosyasındaki başvuru durumu onaylandı olarak güncellenir ve kullanicilar.txt dosyasındaki durumu burslu olarak kaydedilir.
    def burs_basvuru_onayla(self):
        basvurular = GenelIslemler.dosya_okuma(self.get_basvurular())
        kullanicilar = GenelIslemler.dosya_okuma(self.get_kullanicilar())

        print("***** BURS BAŞVURULARI *****".center(120))
        beklemede_burslar = []
        for index, basvuru in enumerate(basvurular):
            bilgiler = basvuru.split(",")
            if bilgiler[0] == "burs" and bilgiler[-1] == "beklemede":
                beklemede_burslar.append((index + 1, bilgiler))

        if not beklemede_burslar:
            print("Henüz beklemede burs başvurusu yok.")
            return

        print("Beklemede olan burs başvuruları: ")
        for numara, bilgiler in beklemede_burslar:
            print(f"{numara}. Kullanıcı Adı: {bilgiler[1]}, İsim Soyisim: {bilgiler[2]}, YKS Puanı: {bilgiler[5]}")

        secim = input("Onaylamak istediğiniz başvuru numarasını giriniz (iptal için 'i' tuşlayın): ").strip()
        if secim.lower() == "i":
            return

        try:
            secim_numara = int(secim) - 1
            if 0 <= secim_numara < len(beklemede_burslar):
                basvuru = beklemede_burslar[secim_numara][1]
                basvuru[6] = "onaylandı"
                basvurular[beklemede_burslar[secim_numara][0] - 1] = ",".join(basvuru)
                kullanici_adi = basvuru[1] 
                for index, kullanici in enumerate(kullanicilar):
                    bilgiler = kullanici.split(",")
                    if bilgiler[2] == kullanici_adi:  
                        bilgiler[-1] = "burslu" 
                        kullanicilar[index] = ",".join(bilgiler)
                        break

                GenelIslemler.dosya_yazma(self.get_basvurular(), basvurular)
                GenelIslemler.dosya_yazma(self.get_kullanicilar(), kullanicilar)
                print(f"{basvuru[2]} isimli öğrencinin burs başvurusu onaylandı ve burs durumu güncellendi.")
            else:
                print("Geçersiz başvuru numarası.")
        except ValueError:
            print("Lütfen geçerli bir numara giriniz.")

    #Burs başvurusu reddedilecek öğrencinin basvurular.txt dosyasındaki başvurusu reddedildi olarak güncellenir.
    def burs_basvuru_reddet(self):
        basvurular = GenelIslemler.dosya_okuma(self.get_basvurular())
        print("***** BURS BAŞVURULARI *****".center(120))
        
        beklemede_burslar = []
        for index, basvuru in enumerate(basvurular):
            bilgiler = basvuru.split(",")
            if bilgiler[0] == "burs" and bilgiler[-1] == "beklemede":
                beklemede_burslar.append((index + 1, bilgiler))

        if not beklemede_burslar:
            print("Henüz beklemede burs başvurusu yok.")
            return

        print("Beklemede olan burs başvuruları: ")
        for numara, bilgiler in beklemede_burslar:
            print(f"{numara}. Kullanıcı Adı: {bilgiler[1]}, İsim Soyisim: {bilgiler[2]}, YKS Puanı: {bilgiler[5]}")

        secim = input("Reddetmek istediğiniz başvuru numarasını giriniz (iptal için i tuşlayın): ")
        if secim.lower() == "i":
            return

        try:
            secim_numara = int(secim) - 1
            if 0 <= secim_numara < len(beklemede_burslar):
                basvuru = beklemede_burslar[secim_numara][1]
                basvuru[6] = "reddedildi"  
                basvurular[beklemede_burslar[secim_numara][0] - 1] = ",".join(basvuru) 
                GenelIslemler.dosya_yazma(self.get_basvurular(), basvurular)
                print(f"{basvuru[2]} burs başvurusu reddedildi.")
            else:
                print("Geçersiz başvuru numarası.")
        except ValueError:
            print("Lütfen geçerli bir numara giriniz.")

    #Personel burs ödemelerini yapabilir. Burs miktarı odemeler.txt dosyasından okunup kullanicilar.txt dosyasındaki burslu durumundaki öğrencilerin bakiyelerine o bakiye eklenir.
    def burs_odeme_yap(self):
        kullanicilar = GenelIslemler.dosya_okuma(self.get_kullanicilar())
        odemeler = GenelIslemler.dosya_okuma(self.get_odemeler())  
        yeni_kullanicilar = []
        burs_ucreti = 0
        for ucret in odemeler:
            tip, miktar = ucret.split(",")
            if tip == "burs":
                burs_ucreti = int(miktar)
                break

        for kullanici in kullanicilar:
            bilgiler = kullanici.split(",")
            if bilgiler[0] == "ogrenci" and bilgiler[-1] == "burslu":
                mevcut_bakiye = int(bilgiler[5])
                yeni_bakiye = mevcut_bakiye + burs_ucreti
                bilgiler[5] = str(yeni_bakiye)
                print(f"{bilgiler[4]} isimli öğrenciye {burs_ucreti} TL burs ödemesi yapıldı. Yeni bakiye: {yeni_bakiye} TL")
            yeni_kullanicilar.append(",".join(bilgiler))

        GenelIslemler.dosya_yazma(self.get_kullanicilar(), yeni_kullanicilar)
        print("Burs ödemeleri tamamlandı!")
        time.sleep(2)
        GenelIslemler.ekran_temizle()

    #Öğrenciler personelden bakiye yüklemelerini isteyebilir. İstenen miktar kullanicilar.txt dosyasındaki bakiye kısmına eklenir. 
    def bakiye_yukle(self):
        GenelIslemler.ekran_temizle()
        print("***** BAKİYE YÜKLE *****".center(120))  
        kullanici_adi = input("Bakiyesi yüklenecek öğrencinin kullanıcı adını giriniz: ").strip()
        mevcut_kullanicilar = GenelIslemler.dosya_okuma(self.get_kullanicilar())
        ogrenci_bulundu = False
        for index, kullanici in enumerate(mevcut_kullanicilar):
            bilgiler = kullanici.split(",")
            if bilgiler[0] == "ogrenci" and bilgiler[2] == kullanici_adi:
                ogrenci_bulundu = True
                try:
                    miktar = int(input("Yüklemek istediğiniz tutarı giriniz (TL): ").strip())
                    if not Personel.gecerli_bakiye_mi(miktar): 
                        print("Lütfen geçerli bir tutar giriniz!")
                        time.sleep(2)
                        return
                    
                    mevcut_bakiye = int(bilgiler[5])
                    yeni_bakiye = mevcut_bakiye + miktar
                    bilgiler[5] = str(yeni_bakiye)  
                    mevcut_kullanicilar[index] = ",".join(bilgiler)
                    
                    GenelIslemler.dosya_yazma(self.get_kullanicilar(), mevcut_kullanicilar)
                    print("Bakiye yükleniyor...")
                    time.sleep(1)
                    print(f"Yükleme başarılı. {kullanici_adi} kullanıcısının yeni bakiyesi: {yeni_bakiye} TL")
                    time.sleep(2)
                    GenelIslemler.ekran_temizle()
                except ValueError:
                    print("Lütfen geçerli bir sayı giriniz.")
                break

        if not ogrenci_bulundu:
            print("Öğrenci kaydı bulunamadı. Lütfen tekrar deneyiniz.")
            time.sleep(2)

    #Personel yurt ödemelerini gerektiğinde sıfırlayabilir. kullanicilar.txt dosyasından ödendi olarak geçen öğrenciler ödenmedi olarak güncellenir. Bu sayede ödemelerin devamlılığı sağlanmış olur.
    def odemeleri_sifirla(self):
        GenelIslemler.ekran_temizle()
        print("***** ÖDEMELERİ SIFIRLA *****".center(120))
        print("Ödemeler sıfırlanıyor. Lütfen bekleyiniz...")
        time.sleep(2)
        yurt_kayitlari = GenelIslemler.dosya_okuma(self.get_yurt_kayitlari())
        yeni_kayitlar = []

        for kayit in yurt_kayitlari:
            bilgiler = kayit.split(",")
            bilgiler[-1] = "ödenmedi"  
            yeni_kayit = ",".join(bilgiler)
            yeni_kayitlar.append(yeni_kayit)

        GenelIslemler.dosya_yazma(self.get_yurt_kayitlari(), yeni_kayitlar)

        print("Öğrenci yurt ödemeleri başarıyla sıfırlandı.")
        input("Devam etmek için \"Enter\" tuşuna basın.")
        GenelIslemler.ekran_temizle()

    #POLYMORİFZM. Personeller için şifre sıfırlama metodu.
    def sifre_sifirla(self):
        print("***** PERSONEL ŞİFRE SIFIRLAMA *****")
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
        print("Şifreniz başarıyla güncellendi.")

    #Bakiye geçerliliğini kontrol eden statik metot. Bakiyenin eksi olup olmadığını kontrol eder. Diğer classlarda da kullanılabilir.
    @staticmethod
    def gecerli_bakiye_mi(bakiye):
        if bakiye >= 0:
            return True
        print("Bakiye negatif olamaz!")
        return False
    
    #Toplam personel sayısını döndüren class metot. kullanicilar.txt dosyasından personeller filtrelenerek taranır. Toplam personel sayısının çıktısı verilir.
    @classmethod
    def toplam_personel_sayisi(cls):
        personel_sayisi = 0
        kullanicilar = GenelIslemler.dosya_okuma(cls.kullanicilar)

        for kullanici in kullanicilar:
            if kullanici.startswith("personel"):
                personel_sayisi += 1

        return f"Sistemde kayıtlı toplam personel sayısı: {personel_sayisi}"