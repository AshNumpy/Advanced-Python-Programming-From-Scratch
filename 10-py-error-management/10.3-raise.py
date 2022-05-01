# x = 10

# if x > 5:
#     raise Exception("'x cant be more than five")

def check_pass(ps):
    import re
    if len(ps) < 8:
        raise Exception('password cant be less than eight')
    
    elif not re.search("[a-z]",ps):
        raise Exception("Pass must include lower case")
    
    elif not re.search("[A-Z]",ps):
        raise Exception("Pass must include upper case")
    
    elif not re.search("[0-9]",ps):
        raise Exception("Pass must include numeric case")

    elif not re.search("[_@$]",ps):
        raise Exception("Pass must include alpha numeric case")

    elif not re.search("[\s]",ps): # \s = space case
        raise Exception("Pass must include space")
    else:
        print("password created")

class Person:
    def __init__(self,name,surname):
        if len(name) < 3:
            raise Exception('name cant be less than threeeeee!!')
        else:
            self.name = name

while True:
    name = input('name: ')
    sName = input('surname: ')

    try:
        person = Person(name,sName)
    except Exception as ex:
        print(ex)
    else:
        break
    finally:
        print('-'*30)
        print('End of the creating person process')

while True:
    password = input('password: ')

    try:
        check_pass(password)
    except Exception as ex:
        print(ex)
    else:
        break
    finally:
        print('-'*30)
        print('end of the creating password process')
