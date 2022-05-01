# error handling 
from setuptools import find_namespace_packages


while True:
    try:
        x = int(input('x:'))
        y = int(input('y:'))
        print(x/y)

    except Exception as ex:
        print("wrong input type ->",ex)

    else:
        print("Good, seems no warning")
        break
    
    finally:
        print("-----------------")
        print('Ending try-except')
#-------------------------------------------------

# except ZeroDivisionError:
#     print('y cant be equal to zero')
    
# except ValueError:
#     print('input only numeric value to x or y')
#-------------------------------------------------

# except (ZeroDivisionError, ValueError) as e :
#     print("trying to wrong input")
#     print('error type: ', e)