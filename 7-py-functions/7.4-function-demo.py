# Gönderilen bir kelimeyi bertilen kez ekranda gösteren bir fonk yazınız.

def word(kelime,itr):
    for i in range(itr):
        print(kelime)

word("ramazan",3)

# Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyon yazınırz.

def getList(*args):
    list=[]
    for i in args:
        list.append(i)

    return list
listem = getList(10,20,30,40,50,60)
print(listem)

# Gönderilen 2 sayı arasındaki tüm asal sayıları bulun
def asalBul(num1,num2):
    for sayi in range(num1,num2):
        if sayi > 1:
            for i in range (2,sayi):
                if (sayi % i == 0):
                    break
            else:
                print(sayi)
                
asalBul(10,30)
# Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndür
def tamBolen(num):
    list = []
    for i in range(2,num):
        if num % i == 0:
            list.append(i)
        else:
            continue

    return list

print(tamBolen(10))