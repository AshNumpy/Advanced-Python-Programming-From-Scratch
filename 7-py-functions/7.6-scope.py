"""
# global scope
x = 'global x'

def func ():
    #local scope
    x = 'local x'

func()
print(x)

"""

########################

name = 'ramazan'

def changeName(new_name):
    name = new_name
    print(name)

changeName('erduran')

print(name)