#------------------------------------------#
list = [1,2,3,4,5]

iterator = iter(list)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

print('-'*50)

for i in list:
    print(i)

print('-'*50)

# Background of the for loop
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

#------------------------------------------#
print('-'*50)

class myNumbers:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration("End of the Iterations...")

myList = myNumbers(10, 15)
myList2 = myNumbers(3, 5)

# Mod 1:
for i in myList:
    print(i)

# Mod 2:
while True:
    try:    
        nums = iter(myList2)
        print(next(nums))
    except StopIteration:
        break