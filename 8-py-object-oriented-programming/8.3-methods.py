# class

from ctypes import addressof


class Person:
    #class attributes
    address = 'no information' # class kullanıldığında girilmesi zorunlu olmayan kısımları buraya yazarız.

    #constructor(yapıcı method)
    def __init__(self, name, year): # class kullanıldığında girilmesi zorunlu olanları buraya yazarız (name, year)
        #object attributes
        self.name = name
        self.birthyear = year
        print("init methodu çalıştı!")

    #instance methods
    def intro(self):
        print("Hello ", self.name)

    def calculateAge(self):
        return 2022 - self.birthyear

# object, instance
p1 = Person('ramazan',2000)
p2 = Person(name = 'emirhan', year = 2005)

p1.intro()
print(f"adım {p1.name} yaşım {p1.calculateAge()}")



class Circle:
    #Class obj. attribute
    pi = 3.14 # Class obj her Circle çağrıldığında ortak değer olarak yer alır.

    def __init__(self,yaricap=1):
        self.r = yaricap
    
    #Methods
    def cevre_hesapla(self):
        return 2*self.pi*self.r
    
    def alan_hesapla (self):
        return self.pi*self.r**2
    
c1 = Circle() #Yarı çap belirtilmezse 1 alınır 
c2 = Circle(5)

print(f"c1: alan = {c1.alan_hesapla()}  çevre= {c1.cevre_hesapla()}")
print(f"c2: yarı çapı: {c2.r} alan = {c2.alan_hesapla()}")
