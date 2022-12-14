import sqlite3
import time
con = sqlite3.connect("kutuphane")
cursor = con.cursor()
class kitap():
    def __init__(self,isim,yazar,yayınevi,tur,baskı):
        self.isim = isim
        self.yazar = yazar
        self.yayınevi = yayınevi
        self.tur = tur
        self.baskı = baskı
    def __str__(self):
        print(self.isim,self.yazar,self.yayınevi,self.tur,self.baskı)
class kutuphane():
    def __init__(self):
        self.baglanti_kur()  #kutuphane çağırılınca direkt veritabanı oluşacak
    def baglanti_kur(self):
        self.baglanti = sqlite3.connect("kutuphane.db")
        self.cursor = self.baglanti.cursor()
        sorgu = "CREATE TABLE IF NOT EXISTS kitaplar (isim TEXT,yazar TEXT,yayınevi TEXT,tur TEXT,baskı INT) "
        self.cursor.execute(sorgu)
        self.baglanti.commit()      #direkt veritanı oluşuyor
    def baglanti_kes(self):
        self.baglanti.close()
    def kitapları_goster(self):
        sorgu = "select * from kitaplar"
        self.cursor.execute(sorgu)
        liste = self.cursor.fetchall()
        if len(liste) == 0:
            print("Kütüphanede kitap bulunmamakta")
        else:
            for a,b,c,d,e in liste:
                print(a,b,c,d,e)
    def kitap_sorugula(self,isim):
        self.cursor.execute("select * from kitaplar where isim = ?",(isim,))
        yazdır = self.cursor.fetchall()
        if len(yazdır) == 0:
            print("aradığınız kitap bulunamadı .")
        else:
            print(yazdır)
    def kitap_ekle(self,kitap):
        sorgu = "Insert into kitaplar values (?,?,?,?,?)"
        self.cursor.execute(sorgu,(kitap.isim,kitap.yazar,kitap.yayınevi,kitap.tur,kitap.baskı))
        self.baglanti.commit()
    def kitap_sil(self,isim):
        sorgu = "delete from kitaplar where isim = ?"
        self.cursor.execute(sorgu,(isim,))          #sondaki ifade tuple yollanmak zorunda yoksa çalışmaz
        self.baglanti.commit()
    def baskı_yukselt(self,isim):
        sorgu = "select * from kitaplar where isim = ?"
        self.cursor.execute(sorgu,(isim,))
        liste = self.cursor.fetchall()
        if len(liste) == 0:
            print("Böyle bir kitap bulunmuyor .")
        else:
            baskı = liste[0][4]     #listenin 1.elemanının 4.indexi baskı
            baskı += 1
            sorgu = "update kitaplar set baskı = ? where isim = ?"
            self.cursor.execute(sorgu,(baskı,isim))
            self.baglanti.commit()