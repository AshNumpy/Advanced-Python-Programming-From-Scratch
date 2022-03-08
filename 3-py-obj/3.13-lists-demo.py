# 1- "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz:
cars=["Bmw","Mercedes","Opel","Mazda"]

# 2- Liste kaç elemanlıdır:
print(len(cars))

# 3-Listenin ilk ve son elemanları nelerdir:
print(cars[0],cars[-1])

# 4- Mazda değerini toyota ile değiştirin:
cars[-1] = "Toyota"
print(cars)

# 5- Mercedes listenin bir elemanı mıdır:
result = "Mercedes" in cars
print(result)

# 6- Listenin -2 indeksindeki değer nedir:
print(cars[-2])

# 7- Listenin ilk 3 elemanını alın:
cars3=cars[0:3]
print(cars3)

# 8- Listenin son iki elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin:
cars[-1] = "Renault"
cars[-2] = "Toyota"
print(cars)

# 9- Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin:
carsNew=cars + ["Audi", "Nissan"]
print(carsNew)
# 10- Listenin son elemanını silin:
del cars[-1]
print(cars)

# 11- Liste elemanlarını tersten yazdırınız:
print(cars[::-1])

# 12- Aşağıdaki verileri bir liste içinde saklayınız:
    
    #studentA: Yiğit Bilgi 2010, (70,60,70)
    #studentB: Sena Turan 1999, (80,80,70)
    #studentC: Ahmet Turan 1998, (80,70,90)

studentA = ["Yiğit","Bilgi",2010,[70,60,70]]
studentB = ["Sena","Turan",1999,[80,80,70]]
studentC = ["Ahmet","Turan",1998,[80,70,90]]

# 13- Liste elemanlarını ekrana yazdırınız:
print(studentA)
print(studentB[-1])
print(studentC[-1][1])

result = f"{studentA[0]} {studentA[1]} {2022-studentA[2]} yaşında ve not ortalaması {int((studentA[-1][0]+studentA[-1][1]+studentA[-1][2])/3)}"
print(result)
