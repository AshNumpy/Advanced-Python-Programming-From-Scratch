names=["Ali","Yağmur","Hakan","Deniz"]
years = [1998,2000,1998,1987]

# 1- "Cenk" ismini listenin sonuna ekleyiniz:
names.append("Cenk")

# 2- "Sena" değerini listenin başına ekleyiniz:
names.insert(0,"Sena")

# 3- "Deniz" ismini listeden siliniz:
names.remove("Deniz")

# 4- "Cenk" isminin indeksi nedir:
result = names.index("Cenk")

# 5- "Ali" listenin bir elemanı mıdır:
result = "Ali" in names
 
# 6- Liste elemanlarını ters çevirin:
names.reverse()

# 7- Listenin elemanlarını alfabetik olarak sıralayınız:
names.sort()

# 8- Years listesini rakamsal olarak büyüklüğe göre sıralayınız:
years.sort()

# 9- str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz:
str= ["Chevrolet","Dacia"]

# 10- Years dizisinin  en büyük ve en küçük elemanı nedir:
result = max(years)
result = min(years)

# 11- Years dizisinde kaç tane 1998 değeri vardır:
result = years.count(1998)

# 12- Years dizisinin tüm elemanlarını siliniz:
years.clear()

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız:
brands = []
brand = input("1. markayı giriniz:")
brands.append(brand) 

brand = input("2. markayı giriniz:")
brands.append(brand) 

brand = input("3. markayı giriniz:")
brands.append(brand) 

print(result)
print(years)
print(brands)