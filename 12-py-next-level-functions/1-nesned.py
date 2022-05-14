"""
def greeting(name):
    print('hello',name)

sayHello = greeting

print(sayHello) # same address
print(greeting)

del sayHello 
print(greeting) # address still exist

#encapsulation
def outer(num1):
    print('outer')
    def inner_increment(num1):
        print('inner')
        return num1 + 1
    num2 = inner_increment(num1)
    print(num1 , num2)

outer(10)
# inner_increment(10) # name error
"""

def factorial(num):
    if not isinstance(num, int):
        raise TypeError("number must be integer!")

    if not num >= 0:
        raise ValueError("number must be zero or positive!")

    def inner_factorial(num):
        if num <= 1:
            return 1
        return num * inner_factorial(num-1)
    
    return inner_factorial(num)

try:
    print(factorial(5))
    print(factorial('a'))

except Exception as e:
    print(e)