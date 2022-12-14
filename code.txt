import time         #zaten içinde vardı kütüphanenin
from sqlveritabanı import *     #mark directory sources root demeliyiz
print("GIRIS YAP")
i = 3
while i>0:
    kadi = input("Kullanıcı adı :")
    if kadi == "name":
        password = input("Şifre :")
        if password == "12345":
            print("Giriş başarılı yönlendiriliyorsun ...")
            time.sleep(3)
            break
        else:
            i -= 1
            if i == 0:
                exit(1)
            print("Şifre hatalı !\n{} hakkın kaldı.Tekrar dene ...  ".format(i))
    else:
        i -= 1
        if i == 0:
            exit(1)
        print("kullanıcı adı hatalı !\n{} hakkın kaldı.Tekrar dene ...  ".format(i))
kutuphane1 = kutuphane()
print("\n\n\n\nKütüphane Işlemleri")
print("1.Kitapları göster\n2.Kitap sorgula\n3.Kitap ekle\n4.Kitap sil\n5.Baskı yükselt\n6.çıkış\n\n")
while True:
    secim = int(input("seçim :"))
    match secim:
        case 1:
            kutuphane1.kitapları_goster()
        case 2:
            isim = input("sorgulanacak kitap ismi :").lower()
            kutuphane1.kitap_sorugula(isim)
        case 3:
            isim = input("Kitap ismi :").lower()
            yazar = input("Kitabın yazarı :").lower()
            yayınevi = input("Kitap yayınevi :").lower()
            tur = input("Kitap türü :").lower()
            baskı = int(input("Kitap baskı :"))
            print("kitap ekleniyor ...")
            time.sleep(2)
            yeni_kitap = kitap(isim,yazar,yayınevi,tur,baskı)
            kutuphane1.kitap_ekle(yeni_kitap)
            print("Kitap eklendi.")
        case 4:
            isim = input("silinecek kitap ismi gir :")
            cevap = input("emin misiniz (e,h):").lower()
            if  cevap == "e":
                print("kitap siliniyor ..")
                time.sleep(2)
                kutuphane1.kitap_sil(isim)
                print("kitap silindi.")
            else:
                continue
        case 5:
            isim = input("Hangi kitabın baskısını yükseltmek istiyorsunuz :")
            kutuphane1.baskı_yukselt(isim)
        case 6:
            print("Program sonlandırılıyor...")
            time.sleep(2)
            exit(1)
        case _:
            print("geçersiz işlem !")