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

    #methods
    """NEXT SUBJ."""

# object, instance
p1 = Person('ramazan',2000)
p2 = Person(name = 'emirhan', year = 2005)

#updating
p2.name = 'emir'

# accessing object attributes
print(f"name: {p1.name} year: {p1.birthyear} address: {p1.address}")
print(f"name: {p2.name} year: {p2.birthyear}")
