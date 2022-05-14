#-----------------------------------------#
def my_decorator(func):
    def wrapper(name):
        print("--before the function--")
        func(name)
        print("--after the function--")
    return wrapper

@my_decorator
def sayHello(name):
    print("Hello",name)

sayHello('Ramazan')

#-----------------------------------------#
print('-'*50)

import math
import time 

def calculateTime(func):
    def wrapper(*args):
        start = time.time()
        time.sleep(1)
        result = func(*args)
        finish = time.time()
        print(f"{func.__name__} processing completed in {round(finish-start,5)} sec. \nResult = {result}\n")
    return wrapper

@calculateTime
def exponentiation(a,b):
    return math.pow(a,b)

@calculateTime
def factorial(a):
    return math.factorial(a)

def plus(a,b): #not tagged
    print(a+b)

exponentiation(2, 5)
factorial(5)
plus(3,4) #not calculated by calculateTime()