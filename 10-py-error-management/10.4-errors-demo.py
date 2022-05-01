from importlib import invalidate_caches
from typing import final


liste = ["1",'2','5a','10b','10','abc']

# 1: Find the numeric values in the 'liste'
for x in liste:
    try:
        print(int(x))
    except Exception as ex:
        continue
print('-'*30)
# 2: Make sure every entry you receive is numeric unless the user enters the 'q' value. 
# Otherwise, print an error message
while True:  
    entry = input('entry: ')

    if entry == 'q':
        print('exiting')
        break
    else:
        try:
            print(int(entry))
            break
        except:
            print('You must input the numeric. Otherwise if you want to quit you input "q"')
            continue
print('-'*30)

# 3: Throw an error that is 'turkish case error' for password which got from user
turkish_cases = 'üğışçöİ'

def checkPass(passw):    
    for i in passw:
        if i in turkish_cases:
            raise ValueError('You cant input the turkish case')
        else:
            next

while True:
    passw = input('password: ')
    try: 
        checkPass(passw)
        print('password created')
        break
    except ValueError as ve:
        print(ve)
print('-'*30)
# 4: Create a factorial function and create error messages 
# for input values of function

def factor(num):
    try:
        num = int(num)
        if num < 0:
            raise ValueError('Number cant be less than zero')
        result = 1
        for i in range(1,num+1):
            result *= i
        print(f'{num} fact: {result}')
    except:
        print(f'"{num}" -> Entry must be numeric')

number = input('number: ')
number = list(number)

for x in number:
    try:
        factor(x)
    except ValueError as ve:
        print(ve)