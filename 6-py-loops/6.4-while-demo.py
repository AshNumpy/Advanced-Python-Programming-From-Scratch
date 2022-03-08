sayilar = [1,3,5,7,9,12,19,21]

# Sayilar listesini while ile ekrana yazdırın
"""i=0
while(i <= len(sayilar)-1 ):
    print(sayilar[i])
    i += 1"""

# Başlangıç ve bitiş değerlerini kullanıcıdan 
#   alıp ekrana tüm tek sayıları yazdırın
"""start = int(input("Başlangıç sayısı: "))
end = int(input("Bitiş sayısı: "))
sayilar2=[]

i = start
while(i <= end):
    if(i % 2 != 0):
        sayilar2.append(i)
    else:
        next
    i += 1

print(sayilar2)"""

# 1-100 arasındaki sayıları azalan şekilde yazdırın
"""i=100

while(i >= 1):
    print(i)
    i -= 1"""

# Kullanıcıdan aldığınız 5 sayıyı ekranda sıralı bir şekilde yazdırın
"""i = 0 
sayilar3 = []

while(i < 5):
    j = int(input("Bir sayi giriniz:"))
    sayilar3.append(j)
    i+=1
print(sayilar3)"""

# Kullanıcıdan alacağınız sınırsız ürün bigisini urunler içinde saklayınız:
#   ** ürün sayısını kullanıcıya sorun
#   ** dictionary listesi yapısı (name,price) şeklinde olsun
#   ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin

urunler = []
itr = int(input("Kaç adet ürününüz var? "))
i=0

while i < itr:
     name = input(f"{i+1}. ürünün ismi:")
     price = input(f"{i+1}. ürünün fiyatı: ")

     urunler.append({
         'name':name,
         'price':price
     })

     i+=1

print("*"*50)
j=1
for i in urunler:
    # print(i)
    print(f"{j}. Ürün adı: {i['name']} \n\t fiyatı: {i['price']}")
    j += 1