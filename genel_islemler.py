import os
import time
#GENEL İŞLEMLER SINIFI: Dosya işlemleri ve menü işlemlerinin tek çatı altında birleştiği sınıf.
class GenelIslemler:
    #Sınıfın constructor metodu.
    def __init__(self):
        self.__kullanicilar = "kullanicilar.txt"
        self.__odemeler = "odemeler.txt"
        self.__duyurular = "duyurular.txt"

    # ---------------------------------------------------------------- Getter ve Setter metotları ---------------------------------------------------------

    def get_kullanicilar(self):
        return self.__kullanicilar

    def set_kullanicilar(self, yeni_dosya):
        self.__kullanicilar = yeni_dosya

    def get_odemeler(self):
        return self.__odemeler

    def set_odemeler(self, yeni_dosya):
        self.__odemeler = yeni_dosya

    def get_duyurular(self):
        return self.__duyurular
    
    def set_duyurular(self,yeni_dosya):
        self.__odemeler = yeni_dosya
    # ---------------------------------------------------------------- Getter ve Setter metotları sonu -------------------------------------------------------

    # Konsolu temizlemek için statik metot. Diğer sınıflarda kullanılabilir. Ekranı temizler. 
    @staticmethod
    def ekran_temizle():
        os.system('cls' if os.name == 'nt' else 'clear')

    #İlgili dosya yolunu döndürmesi için statik metot.
    @staticmethod
    def dosya_yolu(dosya_adi):
        return os.path.join("data", dosya_adi)

    #Dosya yolundan dosya okuma için statik metot. Txt dosyaları okunur. Liste olarak döndürülür. Liste elemanları birer nesnedir.
    @staticmethod
    def dosya_okuma(dosya_adi):
        dosya_yolu = GenelIslemler.dosya_yolu(dosya_adi)
        with open(dosya_yolu, 'r', encoding='utf-8') as dosya:
            return [satir.strip() for satir in dosya.readlines()]
  
    #Dosyaya veri yazan statik metot. Diğer classlar yazılacak verileri bu metotla yazabilir.
    @staticmethod
    def dosya_yazma(dosya_adi, veri_listesi):
        dosya_yolu = GenelIslemler.dosya_yolu(dosya_adi)
        with open(dosya_yolu, 'w', encoding='utf-8') as dosya:
            for veri in veri_listesi:
                dosya.write(veri + '\n')

    #Dosyaya yeni veri ekleyen statik metot. Diğer classlar eklenecek verileri bu metotla ekleyebilir.
    @staticmethod
    def dosya_ekleme(dosya_adi, yeni_veri):
        dosya_yolu = GenelIslemler.dosya_yolu(dosya_adi)
        with open(dosya_yolu, 'a', encoding='utf-8') as dosya:
            dosya.write(yeni_veri + '\n')

    #Ana menüyü gösteren metot. İlgili menülere yönlendirmeler yapar. Aynı zamanda programın başlangıç metodudur.
    def menu_goster(self):
        while True:
            self.ekran_temizle()
            print("****** ÖĞRENCİ YURT VE BURS ÖDEMELERİ SİSTEMİ ******".center(120))
            print("\n1 - YÖNETİCİ GİRİŞİ")
            print("2 - PERSONEL GİRİŞİ")
            print("3 - ÖĞRENCİ GİRİŞİ")
            print("4 - ÖĞRENCİ KAYIT")
            print("5 - ŞİFREMİ UNUTTUM")
            print("6 - DUYURULAR")
            print("7 - YURTLARIN KONTENJAN DURUMU")
            print("8 - SİSTEMDEN ÇIKIŞ")
            secim = input("Lütfen bir seçim yapınız: ")
            if secim == "1":
                self.yonetici_giris()
            elif secim == "2":
                self.personel_giris()
            elif secim == "3":
                self.ogrenci_giris()
            elif secim == "4":
                self.ogrenci_kayit()
            elif secim == "5":
                self.sifre_sifirla()
            elif secim == "6":
                self.duyurular_goster()
            elif secim == "7":
                GenelIslemler.ekran_temizle()
                GenelIslemler.yurt_bos_kontenjan_raporu()
            elif secim == "8":
                print("Sistemden çıkış yapılıyor...")
                break
            else:
                print("Hatalı seçim yaptınız. Tekrar deneyiniz.")

    #Yurt kontenjanlarını tarayan ve rapor veren class metot. yurtlar.txt dosyasında taranan nesnelerin raporu verilir.
    @classmethod
    def yurt_bos_kontenjan_raporu(cls):
        yurtlar = cls.dosya_okuma("yurtlar.txt")
        print("***** YURT BOŞ KONTENJAN RAPORU *****".center(120))
        for yurt in yurtlar:
            bilgiler = yurt.split(",")
            yurt_adi = bilgiler[3]
            toplam_kapasite = bilgiler[4]
            bos_kontenjan = bilgiler[5]
            print(f"Yurt: {yurt_adi}, Kapasite: {toplam_kapasite}, Boş Kontenjan: {bos_kontenjan}")
        input("Geri dönmek için \"enter\"a basın.")

    #Yönetici giriş metodu. Kullanıcı adı şifre kontrol edilir ve yönetici classının menüsüne yönlendirir.
    def yonetici_giris(self):
        from sub_classes.mudur import Mudur
        GenelIslemler.ekran_temizle()
        print("***** YÖNETİCİ GİRİŞİ *****".center(120))
        sifre = input("Lütfen şifrenizi giriniz: ").strip()
        mevcut_kullanicilar = GenelIslemler.dosya_okuma("kullanicilar.txt")
        for kullanici in mevcut_kullanicilar:
            bilgiler = kullanici.split(",")
            if bilgiler[0] == "mudur" and bilgiler[3] == sifre: 
                isim_soyisim = bilgiler[3]
                cinsiyet = bilgiler[4]
                mudur = Mudur(kullanici_adi="admin", sifre=sifre, isim_soyisim=isim_soyisim, cinsiyet=cinsiyet)
                print("Giriş başarılı. Müdür menüsüne yönlendiriliyorsunuz...")
                time.sleep(1)
                GenelIslemler.ekran_temizle()
                mudur.menu_goster()
                return
        print("Hatalı şifre! Tekrar deneyiniz.")
        time.sleep(2)
        GenelIslemler.ekran_temizle()

    #Aktif duyuruları gösteren metot. duyurular.txt dosyasından okunan duyuruların çıktısı verilir.
    def duyurular_goster(self):
        self.ekran_temizle()  
        print("****** DUYURULAR ******".center(120))
        duyurular = GenelIslemler.dosya_okuma(self.get_duyurular())
        if not duyurular:
            print("Henüz yeni duyuru yok. Ana menüye yönlendiriliyorsunuz...")
            time.sleep(1)
            GenelIslemler.ekran_temizle()
        else:
            for index, duyuru in enumerate(duyurular, start=1):
                print(f"{index}. {duyuru.split(',')[1]}")  
        input("Geri dönmek için \"enter\" tuşuna basın.")
        GenelIslemler.ekran_temizle()

    #Personel giriş metodu. Kullanıcı adı şifre kontrol edilir ve personel classının menüsüne yönlendirir.
    def personel_giris(self):
        from sub_classes.personel import Personel
        self.ekran_temizle()
        print("*****PERSONEL GİRİŞİ*****".center(120))
        kullanici_adi = input("Kullanıcı adınız: ")
        sifre = input("Şifreniz: ")
        kullanicilar = self.dosya_okuma(self.get_kullanicilar())
        for kullanici in kullanicilar:
            if kullanici.startswith("personel") and kullanici.split(',')[2] == kullanici_adi and kullanici.split(',')[3] == sifre:
                isim_soyisim = kullanici.split(',')[4]
                cinsiyet = kullanici.split(',')[5]
                personel = Personel(kullanici_adi, sifre, isim_soyisim, cinsiyet)
                if cinsiyet.lower() == "erkek":
                    print(f"Giriş başarılı. Hoşgeldiniz {isim_soyisim} Bey.")
                elif cinsiyet.lower() == "kadın":
                    print(f"Giriş başarılı. Hoşgeldiniz {isim_soyisim} Hanım.")
                time.sleep(1)
                print("Personel menüsüne yönlendiriliyorsunuz...")
                time.sleep(2)
                GenelIslemler.ekran_temizle()
                personel.menu_goster()
                return
        print("Hatalı kullanıcı adı veya şifre! Ana menüye dönülüyor...")
        time.sleep(1.5)
        GenelIslemler.ekran_temizle()
    
    #Öğrenci kaydı yapan metot. Öğrenciden bilgiler alınır. Gerekli koşullar sağlanıyorsa öğrenci, kullanıcılar.txt dosyasına kaydedilir.
    def ogrenci_kayit(self):
        GenelIslemler.ekran_temizle()
        print("***** ÖĞRENCİ KAYIT *****".center(120))
        while True:
            kullanici_adi = input("Kullanıcı adınızı giriniz: ").strip()
            mevcut_kullanicilar = GenelIslemler.dosya_okuma(self.get_kullanicilar())
            kullanici_adi_var_mi = False

            for kullanici in mevcut_kullanicilar:
                if kullanici.split(",")[2] == kullanici_adi:
                    kullanici_adi_var_mi = True
                    break
            if kullanici_adi_var_mi:
                print("Bu kullanıcı adı zaten alınmış. Lütfen başka bir kullanıcı adı seçiniz.")
            else:
                break

        isim_soyisim = input("Ad ve soyadınızı giriniz: ").strip()
        eposta = input("E-posta adresinizi giriniz: ").strip()
        while "@" not in eposta or "." not in eposta:
            print("Lütfen geçerli bir e-posta adresi giriniz.")
            eposta = input("E-posta adresinizi giriniz: ").strip()

        while True:
            sifre = input("Şifrenizi oluşturunuz (en az 4 karakter): ").strip()
            if len(sifre) < 4:
                print("Şifre en az 4 karakter olmalıdır. Lütfen tekrar deneyiniz.")
                continue

            sifre_tekrar = input("Şifrenizi tekrar giriniz: ").strip()
            if sifre != sifre_tekrar:
                print("Şifreler uyuşmuyor. Lütfen tekrar deneyiniz.")
            else:
                break

        cinsiyet = input("Cinsiyetinizi giriniz (Erkek/Kadın): ").strip()
        bakiye = 0 
        burs_durumu = "burssuz"  
        yeni_ogrenci = f"ogrenci,{eposta},{kullanici_adi},{sifre},{isim_soyisim},{bakiye},{cinsiyet},{burs_durumu}"
        GenelIslemler.dosya_ekleme(self.get_kullanicilar(), yeni_ogrenci)
        print("Öğrenci kaydı başarıyla tamamlandı!")
        time.sleep(2)
        GenelIslemler.ekran_temizle()

    #Öğrenci giriş ekranı. Öğrenci kullanıcı adı ve şifresini doğru girerek öğrenci menüsüne yönlendirilir. Yanlışsa ana menüye yönlendirir.
    def ogrenci_giris(self):
        from sub_classes.ogrenci import Ogrenci
        self.ekran_temizle()
        print("*****ÖĞRENCİ GİRİŞİ*****".center(120))
        kullanici_adi = input("Kullanıcı adınız: ")
        sifre = input("Şifreniz: ")

        kullanicilar = self.dosya_okuma(self.get_kullanicilar())
        for kullanici in kullanicilar:
            if kullanici.startswith("ogrenci") and kullanici.split(',')[2] == kullanici_adi and kullanici.split(',')[3] == sifre:
                isim_soyisim = kullanici.split(',')[4]
                bakiye = int(kullanici.split(',')[5])
                cinsiyet = kullanici.split(',')[6]
                ogrenci = Ogrenci(kullanici_adi, sifre, isim_soyisim, bakiye,cinsiyet)
                print(f"Giriş başarılı. Hoşgeldiniz {isim_soyisim}.")
                time.sleep(1)
                print("Öğrenci menüsüne yönlendiriliyorsunuz...")
                time.sleep(2)
                self.ekran_temizle()
                ogrenci.menu_goster()
                return
        print("Hatalı kullanıcı adı veya şifre. Tekrar deneyin.")
        time.sleep(2)

    #Şifre sıfırlama metodu. Sistemde kayıtlı e-posta adresi bulunur. E-posta adresinin kayıtlı olduğu ilgili sınıfa yönlendirme yapılır.
    def sifre_sifirla(self):
        from sub_classes.ogrenci import Ogrenci
        from sub_classes.personel import Personel
        self.ekran_temizle()
        print("***** ŞİFREMİ UNUTTUM *****".center(120))
        eposta = input("Lütfen kayıtlı e-posta adresinizi giriniz: ")

        kullanicilar = self.dosya_okuma(self.get_kullanicilar())
        for kullanici in kullanicilar:
            bilgiler = kullanici.split(',')
            if bilgiler[1] == eposta:
                if bilgiler[0] == "personel":
                    personel = Personel(bilgiler[2], bilgiler[3], bilgiler[4], bilgiler[5])
                    personel.sifre_sifirla()
                elif bilgiler[0] == "ogrenci":
                    ogrenci = Ogrenci(bilgiler[2], bilgiler[3], bilgiler[4], bilgiler[5])
                    ogrenci.sifre_sifirla()
                return
        print("E-posta adresi bulunamadı. Ana menüye yönlendiriliyorsunuz...")
