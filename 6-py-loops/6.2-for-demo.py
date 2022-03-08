sayilar = [1,3,5,7,9,12,15,19,21]

# Sayialr listesindeki hangi sayılar 3'ün katı:
"""for i in sayilar:
    if i%3 == 0:
        print(i)
    else:
        next
"""
# Sayilar listesinde sayıların toplamı kaçtır
"""result = 0
for i in sayilar:
    result = result + i 

print(result)
"""
# Sayılar listesindeki tek sayıların karesini alınız
"""result = 0
for i in sayilar:
    if i%3==0:
        result = i**2
        print(result)
"""


sehirler = ["Kocaeli","İstanbul", "Ankara","İzmir","Rize"]

# Şehirlerden hangileri en fazla 5 karakterlidir
"""for i in sehirler:
    if len(i) <= 5:
        print(i) """

urunler = [
    {"name":"samsung s6" , "price":"3000"},
    {"name":"samsung s7" , "price":"4000"},
    {"name":"samsung s8" , "price":"5000"},
    {"name":"samsung s9" , "price":"6000"},
    {"name":"samsung s10" , "price":"7000"}
]

# Ürünlerin fiyatları toplamı kaçtır
"""toplam = 0
for i in urunler:
    toplam += int(i["price"])

print(toplam)"""

# Ürünlerden fiyatı en fazla 5000 olan ürünleri listeleyin
"""for i in urunler:
    j = int(i["price"])
    if j <= 5000:
        print(i["name"])"""
