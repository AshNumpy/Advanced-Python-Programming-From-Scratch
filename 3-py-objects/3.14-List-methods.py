numbers = [1,10,5,16,4,9,10]
letters = ["a","b","c","d","e"]

val = min(numbers)
val = max(numbers)
val = min(letters)
val = max(letters)

val = numbers[3:6]
val = numbers[:3]
val = numbers[4:]

numbers[4] = 40

numbers.append("49") # listenin sonuna veri ekler
numbers.append(50)

numbers.insert(3,78) # 3. indexe 78 ekler
numbers.insert(-1,52)

numbers.pop(0) # 0. indexteki veriyi siler
numbers.pop(-1) 

numbers.remove(9) # 9 isimli veriyi bulur ve siler
numbers.remove("49")

numbers.sort() # listeyi sıralar ama int str karışık olmamalı
letters.sort()

numbers.reverse()# listeyi ters çevirir
letters.reverse()

print(numbers.count(10)) # liste içindeki 10 isimli veriden kaç tane var
print(letters.count("a"))

numbers.clear() # listeyi komple siler

print(numbers)