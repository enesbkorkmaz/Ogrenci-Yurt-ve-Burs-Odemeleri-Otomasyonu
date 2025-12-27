from abc import ABC, abstractmethod

#Personel,Mudur ve Ogrenci alt classlarına şablon olacak ortak metotları içeren Kullanicilar ana sınıfı.
class Kullanicilar(ABC):
    #----------------------------------------Şablon getter ve setter metotları----------------------
    @abstractmethod
    def get_kullanici_adi(self):
        pass

    @abstractmethod
    def set_kullanici_adi(self, yeni_kullanici_adi):
        pass

    @abstractmethod
    def get_sifre(self):
        pass

    @abstractmethod
    def set_sifre(self, yeni_sifre):
        pass

    @abstractmethod
    def get_isim_soyisim(self):
        pass

    @abstractmethod
    def set_isim_soyisim(self, yeni_isim_soyisim):
        pass
    #---------------------------------------------------------------------------------------------

    #İlgili classın menüsü bu metotla ekrana verilecektir.
    @abstractmethod
    def menu_goster(self):
        pass

    #İlgili altclass şifre sıfırlama işlemlerini bu metotla yapacaktır.
    @abstractmethod
    def sifre_sifirla(self):
        pass
