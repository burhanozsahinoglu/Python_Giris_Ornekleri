# String donusturme ile

print("Pozitif Tam Sayi Tersten Yazdirma")
sayi = int(input("Pozitif tamsayi giriniz:"))
if sayi%1 == 0 and sayi > 0:					
	i = str(sayi)								
	ters = i[::-1] 			
	print(ters)									
else:											
	print("Pozitif Tamsayi girmediniz!")
		
print("2. Yontem")			    # tam sayi girilmese bile cevirme islemi yapilir					
k = str(sayi)		
print(*reversed(k), sep='')


# Ikinci Yontem

print("Pozitif Tam Sayi tersten Yazdirma 2")
sayi = eval(input("Pozitif tamsayi giriniz:"))
if sayi%1 == 0 and sayi > 0:					
	uzunluk = len(str(sayi))					
	i = int(uzunluk)							
	while i > 0:								
		ters = sayi%10							
		sayi = int(sayi/10)						
		print(ters, end='')						
		i = i-1									
else:											
	print("Pozitif Tamsayi Girmediniz!")
