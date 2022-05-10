"""
    Soru: Girilen bir sayının asal olup olmadığını bulun:
        ***Asal sayı 1 ve kendisi hariç tam böleni olmayan sayılara denir.
"""

num = int(input("Bir sayi giriniz:"))
result = True

if num == 1:
    print("'1' Sayısı asal değildir.")
else:
    for i in range(2, num):
        if num % i == 0:
            result = False
            break

    if result == True:
        print("Girdiğiniz sayı asaldır.")

    else:
        print("Girdiğiniz sayı asal değildir.")