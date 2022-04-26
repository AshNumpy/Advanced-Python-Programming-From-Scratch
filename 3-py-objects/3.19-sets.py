fruits = {"orange", "apple", "banana"}

# print(fruits[0]) # indexlenemez

for x in fruits:
    print(x)

fruits.add("cherry")
fruits.update(["mango", "grape"])
fruits.add("apple") # listede olan bir şey tekrar eklenemez
fruits.discard("apple") # apple ı sildi
print(fruits)
fruits.pop() # ilk elemaı sildi
print(fruits)

myList = [1,2,2,2,3,3,3,4,5]

print(myList)
print(set(myList)) # tekrarlayan verileri sildi