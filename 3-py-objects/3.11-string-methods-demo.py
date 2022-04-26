# " Hello world " karakter dizisinin baş ve sondaki boşluk karakterlerini silin:
result = " Hello World "
result = result.strip()
print(result)

# "www.google.com" içerisindeki google bilgisi haricindeki her karakteri silin:
result = "www.google.com"
result = result.lstrip("www.")
result = result.rstrip(".com")
print(result)

result= result.strip("w.com")
print(result)

# "course" karakter dizisinin tüm karakterlerini küçük harf yapın:
result = "course"
result = result.upper()
print(result)

# "www.google.com" içinde kaç tane o harfi var:
result="www.google.com"
cnt = result.count("o")
print(cnt)

# "www.google.com" sitesi www ile başlayıp com ile bitiyor mu:
result="www.google.com"
isFrom=result.startswith("www")
print(isFrom)
isFrom=result.endswith("com")
print(isFrom)

# "www.google.com" içerisinde com ifadesi var mı:
result="www.google.com"
isFrom=result.find("com") #varsa index nosunu verir yoksa -1 yazar
isFrom2=result.find("com",0,10) #0 ile 10. index arasında com var mı diye bakar
print(isFrom)
print(isFrom2)

# "course" içindeki karakterlerin hepsi alfabetik mi:
result="course"
isFrom=result.isalpha() #alfabetik mi 
isFrom2=result.isdigit() #dijital sırada mı 123 gibi 
print(isFrom2)
print(isFrom)

# "Contents" ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyin:
result="Contents"
result=result.center(50,"*")
print(result)

# "  course  " karakterindeki boşlukları "-" ile değiştirin:
result="  course  "
result=result.replace(" ","-")
print(result)

# "Sadık Hoca ile Python öğreniyorum" cümlesini boşluklardan itibaren ayırın:
result="Sadık Hoca ile Python öğreniyorum"
result=result.split(" ")
print(result)
print(result[3])
