def f1(a,b):
    print(a+b)
def f2(a,b):
    print(a*b)
def f3(a,b):
    print(a/b)

def op(value):
    value = value.lower()
    if value == 'f1':
        f1(2,3)
    if value == 'f2':
        f3(2,3)
    if value == 'f3':
        f3(2,3)
    
result = input("What you want to do\nf1 -Plus\nf2- Multiple\nf3 -Divide\n")
op(result)