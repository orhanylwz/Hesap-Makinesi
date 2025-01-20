İlkSayı = int(input("İlk Sayıyı Giriniz. "))
İkinciSayı = int(input("İkinci Sayıyı Giriniz. "))
islem = input("""YAPMAK ISTEDIGINIZ ISLEMI GIRINIZ.
(Toplama: +, Çıkarma: -, Çarpma: x, Bölme: /)""")

if islem == "+":
    print("Sonuç: "+str(İlkSayı+İkinciSayı))
elif islem == "-":
    print("Sonuç: " + str(İlkSayı - İkinciSayı))

elif islem == "x":
    print("Sonuç: " + str(İlkSayı * İkinciSayı))

elif islem == "/":
    print("Sonuç: " + str(İlkSayı / İkinciSayı))