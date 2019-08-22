import sqlite3, os

class Yuzde:
    def ikibucuk(self, dnot):
        sonuc = dnot * (0.05 / 2)
        return sonuc
    
    def bes(self, dnot):
        sonuc = dnot * 0.05
        return sonuc
    
    def on(self, dnot):
        sonuc = dnot * 0.10
        return sonuc
    
    def otuz(self, dnot):
        sonuc = dnot * 0.30
        return sonuc
    
    def elli(self, dnot):
        sonuc = dnot * 0.50
        return sonuc

class dersProgrami:
    def hafta(self):
        dersProg = open("ders_programi", "r")
        print("\n", dersProg.read())
        dersProg.close()
    def pz(self):
        dersProg = open("ders_programi", "r")
        pazartesi = dersProg.readlines()
        for i in range(9):
            print(pazartesi[i], end='')
        dersProg.close()
    def sl(self):
        dersProg = open("ders_programi", "r")
        sali = dersProg.readlines()
        for i in range(9,15):
            print(sali[i], end='')
        dersProg.close()
    def car(self):
        dersProg = open("ders_programi", "r")
        carsamba = dersProg.readlines()
        for i in range(15,18):
            print(carsamba[i], end='')
        dersProg.close()
    def per(self):
        dersProg = open("ders_programi", "r")
        persembe = dersProg.readlines()
        for i in range(18,27):
            print(persembe[i], end='')
        dersProg.close()   
    def cuma(self):
        dersProg = open("ders_programi", "r")
        cuma = dersProg.readlines()
        for i in range(27,36):
            print(cuma[i], end='')
        dersProg.close()                     
        
def program():
    Program = dersProgrami()
    while True:
        ac = ("""
            Haftalik Program Icin [0]
            Pazartesi Icin [1]
            Sali Icin [2]
            Carsamba Icin [3]
            Persembe Icin [4]
            Cuma Icin [5]
            Menuye Donmek Icin [q]""")
        print(ac)
        tercih = input("Tercihinizi Yapiniz: ")
        if tercih == '0':
            Program.hafta()
        elif tercih == '1':
            Program.pz()
        elif tercih == '2':
            Program.sl()
        elif tercih == '3':
            Program.car()
        elif tercih == '4':
            Program.per()
        elif tercih == '5':
            Program.cuma()
        elif tercih == 'q':
            break
        else:
            print("Lutfen 0 ile 5 arasinda bir giris yapiniz...\nCikis icin menu ekranina[q] donmeniz gerekiyor.") 

def ogretim():
    dosya = 'og.sqlite'
    dosyaKontrol = os.path.exists(dosya)
    vt = sqlite3.connect('og.sqlite')
    im = vt.cursor()
    im.execute("""CREATE TABLE IF NOT EXISTS hocalar
    (ad, soyad, iletisim)""")
    
    if not dosyaKontrol:
        im.execute("""INSERT INTO hocalar VALUES
        ("Sezer", "YILDIZ", "sezeryildiz@beykoz.edu.tr - 000 - 0000000")""")
        im.execute("""INSERT INTO hocalar VALUES
        ("Reha", "CAPUTCU", "rehacaputcu@beykoz.edu.tr")""")
        im.execute("""INSERT INTO hocalar VALUES
        ("Gozde Mihran", "ALTINSOY", "gozdemihranaltinsoy@beykoz.edu.tr - 000 - 00000000")""")
        im.execute("""INSERT INTO hocalar VALUES
        ("Gizem", "BALTACI", "gizembaltaci@beykoz.edu.tr")""")
        im.execute("""INSERT INTO hocalar VALUES
        ("Feyza", "ERKAN", "feyzaerkan@beykoz.edu.tr")""")
        vt.commit()
    im.execute("""SELECT * FROM hocalar""")
    veriler = im.fetchall()
    vt.close()
    
    for i in veriler:
        print(i[0], i[1], "/// Iletisim:", i[2], '\n')
        
    print("Gunluk Programlari \n")
    sezer = ("""      
             Carsamba / Oglen 14 - 16.45 arasi Cubuklu
             Persembe / Oglen 12 - 14.45 arasi Cubuklu
             Cuma / Sabah 9 - Oglen 13.45 arasi Cubuklu""")
    reha = ("""
             Pazartesi / Sabah 9 - Oglen 12.45 arasi Lisans - Oglen 13 - 17.45 arasi Cubuklu
             Sali / Sabah 9 - 12.45 ile Oglen 14 - 17.45 arasi Cubuklu""")
    feyza = ("""
             Persembe / Sabah 10 - 12.45 ile Oglen 14 - 16.45 arasi Cubuklu""")
    gozde = ("""
             Pazartesi / Sabah 10 - 12.45 ile Ogleden Sonra 16 - 17.45 arasi Cubuklu
             Sali / Sabah 10 - 14.45 ile Oglen 14 - 17.45 arasi Lisans  
             Persembe / Sabah 9 - 12.45 ile Oglen 12 - 17.45 arasi Cubuklu""")
    gizem = ("""
             Pazartesi / 14 - 17.45 arasi Cubuklu
             Sali / 13 - 14.45 ile 16 - 17.45 arasi Rektorluk
             Carsamba / 14 - 15.45 ile 16 - 17.45 arasi Cubuklu
             Persembe / 9 - 10.45 ile 11 - 12.45  ile 14 - 15.45 arasi Cubuklu
             Cuma / 11 - 12.45 ile 14 - 15.45 ile 16 - 17.45 arasi Cubuklu""")
    
    program = ('Sezer YILDIZ',sezer, '\n', 'Reha CAPUTCU',reha, '\n', 'Feyza ERKAN',feyza, '\n', 'Gozde Mihran ALTINSOY',gozde, '\n', 'Gizem BALTACI',gizem, '\n')
    for i in program:
        print(i, sep='')

def guz():

    dersler=("""
    	  Siber Guvenlige Giris: [1]
    	  Programlama Temelleri ve Algoritma: [2]
    	  Ingilizce I: [3]
    	  Bilisim Hukuku: [4]
    	  Matematik: [5]
    	  Veritabani Tasarimi: [6]
    	  Sektorel Cozumler: [7]
          
          Menuye Donus Yapmak Icin: [q] - Cikis Yapmak Icin Menu Ekranina Donmeniz Gerekiyor.
    	  """)

    secimKontrol = 0
    while secimKontrol <= 7:
        
        print(dersler)
        secim = input("Hesaplamak Istediginiz Dersin Numarasini Giriniz: ")
        
        dnot = []
        yuzde = Yuzde()
        
    
        if secim == '1':
            ders1 = 'Siber Guvenlige Giris'
            print("\n", ders1)
            k = 0
            while True:
                try:
                    ksinav1 = int(input("Kucuk Sinav 1 Puaniniz:"))
                    ksinav2 = int(input("Kucuk Sinav 2 Puaniniz:"))
                    odev1 = int(input("Odev 1 Puaniniz:"))
                    odev2 = int(input("Odev 2 Puaniniz:"))
                    vize = int(input("Vize Puaniniz:"))
                    final = int(input("Final Puaniniz:"))
                    k = 1
                    if k == 1:
                        break
                except ValueError:
                    print("HATA! Sadece 1 ile 100 arasinda sayisal deger girilmelidir.\nPuanlarinizi en bastan giriniz!")
            
            dnot.append(ksinav1)
            dnot.append(ksinav2)
            dnot.append(odev1)
            dnot.append(odev2)
            dnot.append(vize)
            dnot.append(final)
            
            for i in range(len(dnot)):
                if dnot[i] < 0 or dnot[i] > 100:
                    print("\nUYARI: 0'dan kucuk, 100'den buyuk puan girilemez.")
                    if i == 0:
                        ksinav1 = int(input("Kucuk Sinav 1 Puaninizi Yeniden Giriniz:"))
                        dnot[i] = ksinav1
                    elif i == 1:
                        ksinav2 = int(input("Kucuk Sinav 2 Puaninizi Yeniden Giriniz:"))
                        dnot[i] = ksinav2
                    elif i == 2:
                        odev1 = int(input("Odev 1 Puaninizi Yeniden Giriniz:"))
                        dnot[i] = odev1
                    elif i == 3:
                        odev2 = int(input("Odev 2 Puaninizi Yeniden Giriniz:"))
                        dnot[i] = odev2
                    elif i == 4:
                        vize = int(input("Vize Puaninizi Yeniden Giriniz:"))
                        dnot[i] = vize
                    elif i == 5:
                        final = int(input("Final Puaninizi Yeniden Giriniz:"))
                        dnot[i] = final

            
            ksinav1 = yuzde.bes(int(dnot[0]))
            ksinav2 = yuzde.bes(int(dnot[1]))
            odev1 = yuzde.bes(int(dnot[2]))
            odev2 = yuzde.bes(int(dnot[3]))
            vize = yuzde.otuz(int(dnot[4]))
            final = yuzde.elli(int(dnot[5]))
            
            print('#'*58, '\n', ders1)
            print("""
                  Kucuk Sinav 1 Notunuz: {}
                  Kucuk Sinav 2 Notunuz: {}
                  Odev 1 Notunuz: {}
                  Odev 2 Notunuz: {}
                  Vize Notunuz: {}
                  Final Notunuz: {}""".format(ksinav1, ksinav2, odev1, odev2, vize, final))
            siberNot = ksinav1+ksinav2+odev1+odev2+vize+final
            print(ders1, "Genel Not Ortalamaniz:", round((siberNot)+0.1))
            print('#'*58,'\n')
            secimKontrol += 1
            ortalama = open("Genel_Not_Ortalamaniz.txt", "a")
            ortalama.write("""
                Siber Guvenlige Giris
                           Kucuk Sinav 1 Notunuz: {}
                           Kucuk Sinav 2 Notunuz: {}
                           Odev 1 Notunuz: {}
                           Odev 2 Notunuz: {}
                           Vize Notunuz: {}
                           Final Notunuz: {}
                Siber Guvenlige Giris Genel Not Ortalamaniz: {}\n""".format(ksinav1, ksinav2, odev1, odev2, vize, final, siberNot))
            ortalama.close()
        
        elif secim == '2':
            ders2 = "Programlama Temelleri ve Algoritma"
            print("\n", ders2)
            ksinav1 = int(input("Kucuk Sinav 1 Puaniniz:"))
            ksinav2 = int(input("Kucuk Sinav 2 Puaniniz:"))
            odev = int(input("Odev Puaniniz:"))
            vize = int(input("Vize Puaniniz:"))
            final = int(input("Final Puaniniz:"))
            
            dnot.append(ksinav1)
            dnot.append(ksinav2)
            dnot.append(odev)
            dnot.append(vize)
            dnot.append(final)
            
            for i in range(len(dnot)):
                if dnot[i] < 0 or dnot[i] > 100:
                    print("\nUYARI: 0'dan kucuk, 100'den buyuk puan girilemez.")
                    if i == 0:
                        ksinav1 = int(input("Kucuk Sinav 1 Puaninizi Yeniden Giriniz:"))
                        dnot[i] = ksinav1
                    elif i == 1:
                        ksinav2 = int(input("Kucuk Sinav 2 Puaninizi Yeniden Giriniz:"))
                        dnot[i] = ksinav2
                    elif i == 2:
                        odev = int(input("Odev Puaninizi Yeniden Giriniz:"))
                        dnot[i] = odev
                    elif i == 3:
                        vize = int(input("Vize Puaninizi Yeniden Giriniz:"))
                        dnot[i] = vize
                    elif i == 4:
                        final = int(input("Final Puaninizi Yeniden Giriniz:"))
                        dnot[i] = final
           
            ksinav1 = yuzde.bes(int(dnot[0]))
            ksinav2 = yuzde.bes(int(dnot[1]))
            odev = yuzde.on(int(dnot[2]))
            vize = yuzde.otuz(int(dnot[3]))
            final = yuzde.elli(int(dnot[4]))
        
            print('#'*58, '\n', ders2)
            print("""
                  Kucuk Sinav 1 Notunuz: {}
                  Kucuk Sinav 2 Notunuz: {}
                  Odev Notunuz: {}
                  Vize Notunuz: {}
                  Final Notunuz: {}""".format(ksinav1, ksinav2, odev, vize, final))
            programNot = ksinav1+ksinav2+odev+vize+final
            print(ders2, "Genet Not Ortalamaniz:", round((programNot)+0.1))
            print('#'*58,'\n')
            secimKontrol += 1
            ortalama = open("Genel_Not_Ortalamaniz.txt", "a")
            ortalama.write("""
                Programlama Temelleri ve Algoritma
                           Kucuk Sinav 1 Notunuz: {}
                           Kucuk Sinav 2 Notunuz: {}
                           Odev Notunuz: {}
                           Vize Notunuz: {}
                           Final Notunuz: {}
                Programlama Temelleri ve Algoritma Genel Not Ortalamaniz: {}\n""".format(ksinav1, ksinav2, odev, vize, final, programNot))
            ortalama.close()
            
        elif secim == '3':
            ders3 = "Ingilizce 1"
            print("\n", ders3)
            ksinav1 = int(input("Kucuk Sinav 1 Puaniniz:"))
            ksinav2 = int(input("Kucuk Sinav 2 Puaniniz:"))
            odev = int(input("Odev Puaniniz:"))
            vize = int(input("Vize Puaniniz:"))
            final = int(input("Final Puaniniz:"))
            
            dnot.append(ksinav1)
            dnot.append(ksinav2)
            dnot.append(odev)
            dnot.append(vize)
            dnot.append(final)
            
            for i in range(len(dnot)):
                if dnot[i] < 0 or dnot[i] > 100:
                    print("\nUYARI: 0'dan kucuk, 100'den buyuk puan girilemez.")
                    if i == 0:
                        ksinav1 = int(input("Kucuk Sinav 1 Puaninizi Yeniden Giriniz:"))
                        dnot[i] = ksinav1
                    elif i == 1:
                        ksinav2 = int(input("Kucuk Sinav 2 Puaninizi Yeniden Giriniz:"))
                        dnot[i] = ksinav2
                    elif i == 2:
                        odev = int(input("Odev Puaninizi Yeniden Giriniz:"))
                        dnot[i] = odev
                    elif i == 3:
                        vize = int(input("Vize Puaninizi Yeniden Giriniz:"))
                        dnot[i] = vize
                    elif i == 4:
                        final = int(input("Final Puaninizi Yeniden Giriniz:"))
                        dnot[i] = final
            
            ksinav1 = yuzde.bes(int(dnot[0]))
            ksinav2 = yuzde.bes(int(dnot[1]))
            odev = yuzde.on(int(dnot[2]))
            vize = yuzde.otuz(int(dnot[3]))
            final = yuzde.elli(int(dnot[4]))
            
            print('#'*58 ,'\n', ders3)
            print("""
                  Kucuk Sinav 1 Notunuz: {}
                  Kucuk Sinav 2 Notunuz: {}
                  Odev Notunuz: {}
                  Vize Notunuz: {}
                  Final Notunuz: {}""".format(ksinav1, ksinav2, odev, vize, final))
            ingNot = ksinav1+ksinav2+odev+vize+final
            print(ders3, "Genel Not Ortalamaniz:", round((ingNot)+0.1))
            print('#'*58,'\n')
            secimKontrol += 1
            ortalama = open("Genel_Not_Ortalamaniz.txt", "a")
            ortalama.write("""
                Ingilizce 1
                           Kucuk Sinav 1 Notunuz: {}
                           Kucuk Sinav 2 Notunuz: {}
                           Odev Notunuz: {}
                           Vize Notunuz: {}
                           Final Notunuz: {}
                Ingilizce 1 Genel Not Ortalamaniz: {}\n""".format(ksinav1, ksinav2, odev, vize, final, ingNot))
            ortalama.close()
            
        elif secim == '4':
            ders4 = "Bilisim Hukuku"
            print("\n", ders4)
            ksinav = int(input("Kucuk Sinav Puaniniz:"))
            odev = int(input("Odev Puaniniz:"))
            sunum = int(input("Sunum Puaniniz:"))
            vize = int(input("Vize Puaniniz:"))
            final = int(input("Final Puaniniz:"))
            
            dnot.append(ksinav)
            dnot.append(odev)
            dnot.append(sunum)
            dnot.append(vize)
            dnot.append(final)
            
            for i in range(len(dnot)):
                if dnot[i] < 0 or dnot[i] > 100:
                    print("\nUYARI: 0'dan kucuk, 100'den buyuk puan girilemez.")
                    if i == 0:
                        ksinav = int(input("Kucuk Sinav Puaninizi Yeniden Giriniz:"))
                        dnot[i] = ksinav
                    elif i == 1:
                        odev = int(input("Odev Puaninizi Yeniden Giriniz:"))
                        dnot[i] = odev
                    elif i == 2:
                        sunum = int(input("Sunum Puaninizi Yeniden Giriniz:"))
                        dnot[i] = sunum
                    elif i == 3:
                        vize = int(input("Vize Puaninizi Yeniden Giriniz:"))
                        dnot[i] = vize
                    elif i == 4:
                        final = int(input("Final Puaninizi Yeniden Giriniz:"))
                        dnot[i] = final             
           
            ksinav = yuzde.bes(int(dnot[0]))
            odev = yuzde.bes(int(dnot[1]))
            sunum = yuzde.on(int(dnot[2]))
            vize = yuzde.otuz(int(dnot[3]))
            final = yuzde.elli(int(dnot[4]))
        
            print('#'*58, '\n', ders4)
            print("""
                  Kucuk Sinav Notunuz: {}
                  Odev Notunuz: {}
                  Sunum Notunuz: {}
                  Vize Notunuz: {}
                  Final Notunuz: {}""".format(ksinav, odev, sunum, vize, final))
            hukukNot = ksinav+odev+sunum+vize+final
            print(ders4, "Genel Not Ortalamaniz:", round((hukukNot)+0.1))
            print('#'*58,'\n')
            secimKontrol += 1
            ortalama = open("Genel_Not_Ortalamaniz.txt", "a")
            ortalama.write("""
                Bilisim Hukuku
                           Kucuk Sinav 1 Notunuz: {}
                           Kucuk Sinav 2 Notunuz: {}
                           Odev Notunuz: {}
                           Sunum Notunuz: {}
                           Vize Notunuz: {}
                           Final Notunuz: {}
                Bilisim Hukuku Genel Not Ortalamaniz: {}\n""".format(ksinav1, ksinav2, odev, sunum, vize, final, hukukNot))
            ortalama.close()
            
        elif secim == '5':
            ders5 = "Matematik"
            print("\n", ders5)
            ksinav1 = int(input("Kucuk Sinav 1 Puaniniz:"))
            ksinav2 = int(input("Kucuk Sinav 2 Puaniniz:"))
            odev = int(input("Odev Puaniniz:"))
            vize = int(input("Vize Puaniniz:"))
            final = int(input("Final Puaniniz:"))
            
            dnot.append(ksinav1)
            dnot.append(ksinav2)
            dnot.append(odev)
            dnot.append(vize)
            dnot.append(final)
            
            for i in range(len(dnot)):
                if dnot[i] < 0 or dnot[i] > 100:
                    print("\nUYARI: 0'dan kucuk, 100'den buyuk puan girilemez.")
                    if i == 0:
                        ksinav1 = int(input("Kucuk Sinav 1 Puaninizi Yeniden Giriniz:"))
                        dnot[i] = ksinav1
                    elif i == 1:
                        ksinav2 = int(input("Kucuk Sinav 2 Puaninizi Yeniden Giriniz:"))
                        dnot[i] = ksinav2
                    elif i == 2:
                        odev = int(input("Odev Puaninizi Yeniden Giriniz:"))
                        dnot[i] = odev
                    elif i == 3:
                        vize = int(input("Vize Puaninizi Yeniden Giriniz:"))
                        dnot[i] = vize
                    elif i == 4:
                        final = int(input("Final Puaninizi Yeniden Giriniz:"))
                        dnot[i] = final
           
            ksinav1 = yuzde.bes(int(dnot[0]))
            ksinav2 = yuzde.bes(int(dnot[1]))
            odev = yuzde.on(int(dnot[2]))
            vize = yuzde.otuz(int(dnot[3]))
            final = yuzde.elli(int(dnot[4]))
        
            print('#'*58, '\n', ders5)
            print("""
                  Kucuk Sinav 1 Notunuz: {}
                  Kucuk Sinav 2 Notunuz: {}
                  Odev Notunuz: {}
                  Vize Notunuz: {}
                  Final Notunuz: {}""".format(ksinav1, ksinav2, odev, vize, final))
            matNot = ksinav1+ksinav2+odev+vize+final
            print(ders5, "Genel Not Ortalamaniz:", round((matNot)+0.1))
            print('#'*58,'\n')
            secimKontrol += 1
            ortalama = open("Genel_Not_Ortalamaniz.txt", "a")
            ortalama.write("""
                Matematik
                           Kucuk Sinav 1 Notunuz: {}
                           Kucuk Sinav 2 Notunuz: {}
                           Odev Notunuz: {}
                           Vize Notunuz: {}
                           Final Notunuz: {}
                Matematik Genel Not Ortalamaniz: {}\n""".format(ksinav1, ksinav2, odev, vize, final, matNot))
            ortalama.close()
        
        elif secim == '6':
            ders6 = "Veritabani Tasarimi"
            print("\n", ders6)
            ksinav1 = int(input("Kucuk Sinav 1 Puaniniz:"))
            ksinav2 = int(input("Kucuk Sinav 2 Puaniniz:"))
            odev1 = int(input("Odev 1 Puaniniz:"))
            odev2 = int(input("Odev 2 Puaniniz:"))
            proje = int(input("Proje Puaniniz:"))
            vize = int(input("Vize Puaniniz:"))
            final = int(input("Final Puaniniz:"))
            
            dnot.append(ksinav1)
            dnot.append(ksinav2)
            dnot.append(odev1)
            dnot.append(odev2)
            dnot.append(proje)
            dnot.append(vize)
            dnot.append(final)
            
            for i in range(len(dnot)):
                if dnot[i] < 0 or dnot[i] > 100:
                    print("\nUYARI: 0'dan kucuk, 100'den buyuk puan girilemez.")
                    if i == 0:
                        ksinav1 = int(input("Kucuk Sinav 1 Puaninizi Yeniden Giriniz:"))
                        dnot[i] = ksinav1
                    elif i == 1:
                        ksinav2 = int(input("Kucuk Sinav 2 Puaninizi Yeniden Giriniz:"))
                        dnot[i] = ksinav2
                    elif i == 2:
                        odev1 = int(input("Odev 1 Puaninizi Yeniden Giriniz:"))
                        dnot[i] = odev1
                    elif i == 3:
                        odev2 = int(input("Odev 2 Puaninizi Yeniden Giriniz:"))
                        dnot[i] = odev2
                    elif i == 4:
                        proje = int(input("Proje Puaninizi Yeniden Giriniz:"))
                        dnot[i] = proje
                    elif i == 5:
                        vize = int(input("Vize Puaninizi Yeniden Giriniz:"))
                        dnot[i] = vize
                    elif i == 6:
                        final = int(input("Final Puaninizi Yeniden Giriniz:"))
                        dnot[i] = final                   
            
            ksinav1 = yuzde.bes(int(dnot[0]))
            ksinav2 = yuzde.bes(int(dnot[1]))
            odev1 = yuzde.ikibucuk(int(dnot[2]))    
            odev2 = yuzde.ikibucuk(int(dnot[3]))    
            proje = yuzde.bes(int(dnot[4]))    
            vize = yuzde.otuz(int(dnot[5]))    
            final = yuzde.elli(int(dnot[6]))
        
            print('#'*58, '\n', ders6)
            print("""
                Kucuk Sinav 1 Notunuz: {}
                Kucuk Sinav 2 Notunuz: {}
                Odev 1 Notunuz: {}
                Odev 2 Notunuz: {}
                Proje Notunuz: {}
                Vize Notunuz: {}
                Final Notunuz: {}""".format(ksinav1, ksinav2, odev1, odev2, proje, vize, final))
            veriNot = ksinav1+ksinav2+odev1+odev2+proje+vize+final
            print(ders6, "Genel Not Ortalamaniz:", round((veriNot)+0.1))
            print('#'*58,'\n')
            secimKontrol += 1
            ortalama = open("Genel_Not_Ortalamaniz.txt", "a")
            ortalama.write("""
                Veritabani Tasarimi
                           Kucuk Sinav 1 Notunuz: {}
                           Kucuk Sinav 2 Notunuz: {}
                           Odev 1 Notunuz: {}
                           Odev 2 Notunuz: {}
                           Proje Notunuz: {}
                           Vize Notunuz: {}
                           Final Notunuz: {}
                Veritabani Tasarimi Genel Not Ortalamaniz: {}\n""".format(ksinav1, ksinav2, odev1, odev2, proje, vize, final, veriNot))
            ortalama.close()
            
        elif secim == '7':
            ders7 = "Sektorel Cozumler"
            print("\n", ders7)
            ksinav1 = int(input("Kucuk Sinav 1 Puaniniz:"))
            ksinav2 = int(input("Kucuk Sinav 2 Puaniniz:"))
            proje = int(input("Proje Puaniniz:"))
            vize = int(input("Vize Puaniniz:"))
            final = int(input("Final Puaniniz:"))
            
            dnot.append(ksinav1)
            dnot.append(ksinav2)
            dnot.append(proje)
            dnot.append(vize)
            dnot.append(final)
            
            for i in range(len(dnot)):
                if dnot[i] < 0 or dnot[i] > 100:
                    print("\nUYARI: 0'dan kucuk, 100'den buyuk puan girilemez.")
                    if i == 0:
                        ksinav1 = int(input("Kucuk Sinav 1 Puaninizi Yeniden Giriniz:"))
                        dnot[i] = ksinav1
                    elif i == 1:
                        ksinav2 = int(input("Kucuk Sinav 2 Puaninizi Yeniden Giriniz:"))
                        dnot[i] = ksinav2
                    elif i == 2:
                        proje = int(input("Proje Puaninizi Yeniden Giriniz:"))
                        dnot[i] = proje
                    elif i == 3:
                        vize = int(input("Vize Puaninizi Yeniden Giriniz:"))
                        dnot[i] = vize
                    elif i == 4:
                        final = int(input("Final Puaninizi Yeniden Giriniz:"))
                        dnot[i] = final
           
            ksinav1 = yuzde.bes(int(dnot[0]))
            ksinav2 = yuzde.bes(int(dnot[1]))
            proje = yuzde.on(int(dnot[2]))
            vize = yuzde.otuz(int(dnot[3]))
            final = yuzde.elli(int(dnot[4]))
        
            print('#'*58,'\n', ders7)
            print("""
                  Kucuk Sinav 1 Notunuz: {}
                  Kucuk Sinav 2 Notunuz: {}
                  Proje Notunuz: {}
                  Vize Notunuz: {}
                  Final Notunuz: {}""".format(ksinav1, ksinav2, proje, vize, final))
            sektorNot = ksinav1+ksinav2+proje+vize+final
            print(ders7, "Genel Not Ortalamaniz:", round((sektorNot)+0.1))
            print('#'*58,'\n')
            secimKontrol += 1
            ortalama = open("Genel_Not_Ortalamaniz.txt", "a")
            ortalama.write("""
                Sektorel Cozumler
                           Kucuk Sinav 1 Notunuz: {}
                           Kucuk Sinav 2 Notunuz: {}
                           Proje Notunuz: {}
                           Vize Notunuz: {}
                           Final Notunuz: {}
                Sektorel Cozumler Genel Not Ortalamaniz: {}\n""".format(ksinav1, ksinav2, proje, vize, final, sektorNot))
            ortalama.close()
            
        elif secim == 'q':
            #print("Cikis...")
            break
            
        else:
            print("Hatali Giris: 1 ile 7 arasinda bir secim yapmalisiniz.")
            
#        if secimKontrol == 7:
#            notlar = open("Genel_Not_Ortalamaniz.txt", "w")
#            notlar.write(siberNot)
#            notlar.close()
        
def bahar():
    print("\nUYARI: Bahar Donemi Dersleri Yakinda Eklenecek.")
#    dersler=("""
#    	  Bilgisayar Aglari: [1]
#    	  Ingilizce 2: [2]
#    	  Nesne Tabanli Programlama: [3]
#    	  Guvenli Web Yazilimi Gelistirme: [4]
#    	  Mesleki Matematik: [5]
#    	  Sunucu Sistemleri Yonetimi: [6]
#    	  Sistem Analizi ve Tasarimi: [7]
#          Secmeli Ders: [8]
#          
#          Donem Secimi Yapmak Icin: [q] - Cikis Yapmak Icin Menu Ekranina Donmeniz Gerekiyor.
#    	  """)
#    
#    secimKontrol = 0
#    while secimKontrol <= 7:  
#        print(dersler)
    
print("""
	  ####################################################	  
	                                                 	 
               Beykoz Universitesi
               Bilgi Guvenligi Teknolojisi Bolumu
               Ders ve Genel Not Ortalamasi Hesaplama ve
               Ogrenci Bilgilendirme Programi
	    	 	 	  	                     	 
	  ####################################################
	  """)

menu=("""
          MENU
          
      Guz Donemi Dersleri Not Hesaplamasi Icin [1]
      Bahar Donemi Dersleri Not Hesaplamasi Icin [2]
      Ders Programiniz Icin [3]
      Ogretim Gorevlilerinin Bilgileri Icin [4]
      
      Cikis Yapmak Icin: [q]""")
print("\nCikis Yapmak Icin: [q]")

   
while True:
    print(menu)
    secim = input("Yapmak Istediginiz Islem Icin Secim Yapiniz: ")
    
    if secim == '1':
        print("\nGuz Donemi Dersleri")
        guz() 
    elif secim == '2':
        #print('\nUYARI: Bahar Donemi Dersleri Yakinda Eklenecek.')
        bahar()
    elif secim == '3':
        program()
    elif secim == '4':
        print('\nOgretim Gorevlileri\n')
        ogretim()
    elif secim == 'q':
        print("Cikis...")
        break
    else:
        print("\nHATALI GIRIS: Sadece 1-2-3-4 arasinda bir secim yapabilirsiniz.\nCikis yapmak icin: [q]")
