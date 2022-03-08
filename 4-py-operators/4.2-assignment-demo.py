x,y,z=2,5,10

numbers = 1,5,7,10,6

# Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z nin toplamının farkı nedir
"""a=int(input("1. sayi:"))
b=int(input("2. sayi:"))
result = a*b
result -= (x+y+z)"""

# y'nin x'e bölümünü hesaplayınız
result = y/x

# (x,y,z) toplamının mod 3' ü nedir
result = x+y+z
result %= 3

# y'nin x. kuvvetini hesaplayınız
result = y**x

#x, *y, z = numbers işlemine göre z'nin küpü kaçtır
x, *y, z = numbers
print(z**3)

#x, y, *z = numbers işlemine göre z'nin değerleri toplamı kaçytır
x, y, *z = numbers

print(numbers)
print(x,y,z)
print(sum(z))