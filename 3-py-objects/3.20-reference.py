# Vale types => string, float, integer

x=5
y=20

x=y
y=10
# print(x,y)

# reference types = > list

a= ["apple","banana"]
b= ["apple","banana"]

a=b
b[0] = "grape" # sadece b üzerinde değişiklik yapsak da a yı etkiledi

print(a,b)