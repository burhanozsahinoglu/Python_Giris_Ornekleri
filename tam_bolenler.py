sayi = int(input("Pozitif tamsayi giriniz:"))
print(sayi, "tamsayisinin tam bolenleri:")

for i in range(2,int((sayi+1)/2)):
    if sayi%i == 0:
        print(i,end='-')
print(sayi)
