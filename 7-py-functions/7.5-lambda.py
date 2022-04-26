#def square(num): return num**2

numbers = [1,2,3,4,5]

#result = list(map(square,numbers))

# for i in map(square,numbers):
#     print(i)

#result  = list(map(lambda num: num**2 , numbers))

#square = lambda num: num**2 

def check_even(num): return num%2 == 0 
#result = list(filter(check_even,numbers))

result = list(filter(lambda num: num%2 == 0, numbers))

print(result)

