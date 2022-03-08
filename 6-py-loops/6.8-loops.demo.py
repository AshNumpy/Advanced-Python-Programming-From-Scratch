"""
    1-100 arasında rasgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile 
    buldurmaya çalışın. (Hak = 5)
    ** "random" modülü için "python random" şeklinde search edin.
    ** 100 üzerinden puanlama yapın. Her soru 20 puan.
    ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı
    üzerinden hesaplansın
"""

import random as rn

print("Hedef sayıyı tahmin etme oyunu")
print("*"*50)
print(">>>Belirtilen kadar hakkınız bulunmaktadır.")
print(">>>Her yanlış tahmin, doğru tahminde alacağınız puanı yüzdelik olarak azaltır:")
print("\t BKZ: Hak:5 - 1. 2. deneme hatalı - 3. tahmin doğru: %60 puan.")

num = rn.randint(1,100)

itr = int(input("Kaç hak olsun? "))
itr2 = itr
i=1 
while(i<=itr):
    guess = int(input("Tahmininiz: "))

    if( guess < num):
        itr2 -= 1
        print(f"Hedef daha yukarıda. \nKalan hakkınız: {itr2}")
        result = False
    elif( guess > num):
        itr2 -= 1
        print(f"Hedef daha aşağıda. \nKalan hakkınız: {itr2}")
        result = False
    else:
        print("Tebrikler sayıyı buldunuz!!!")
        result = True
        ks = 100/itr 
        point = ks*itr2
        break
    i += 1


if result == True:
    print(">"*50)
    print(f"Hedef sayı {num} idi.\nPuan: {point}/100")
else:
    print(f"Üzülme üzülme hede {num} idi. \n Puan: 0")