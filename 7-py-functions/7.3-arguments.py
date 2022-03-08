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
