def changeName(n):
    n = 'ramazan'

name = 'Ahmet'

changeName(name)
print(name)
#************************************

def change(n):
    n[0] = 'İstanbul'

cities = ['Ankara','İzmir','Antalya']

change(cities)
print(cities)
#***********************************
"""
sehirler = ['Ankara','İzmir']
n = sehirler

n[0] = 'İstanbul'
print(sehirler)
"""
#***********************************

sehirler = ['Ankara','İzmir']
n = sehirler[:]

n[0] = 'İstanbul'
print(sehirler)
#***********************************

def add(*params): # gönderilen argümanlar liste olarak alınır.
    return sum(params)

print(add(10,20))
print(add(1,2,3,4,5,6))
#***********************************

def add2(*params):
    sum=0
    for i in params:
        sum += i
    return sum

print(add2(1,2,3))
#***********************************

def myFunc(a,b,*args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

# **kwargs parametresi dictionary olarak verileri alır.
# *args  parametresi ise tuple olarak verileri alır.

myFunc(10,20,30,40,"a",True,key1="Value 1", key2="Value 2")
#**********************************************************

