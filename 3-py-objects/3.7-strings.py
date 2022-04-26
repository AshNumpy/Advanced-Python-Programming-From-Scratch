name = 'Sadık'
surname = "Turan"
age = 36

# print("My name is " + name + " " + surname)
# print("I am " + str(age) + " years old")

greeting = "My name is "+name+" "+ surname + " and \nI am "+ str(age) + " years old"

# print(greeting[2])
# print(len(greeting))
# # print(greeting[-1])
# # print(greeting[2:7]) # 2. index ve 7. index dahil değil
# print(greeting[2:40:2]) # 2 den 40 a kadar 2 şer 2 şer gider

course = "Sadık hoca ile python öğreniyorum"

result = course[::-1] # Course verilerini tersten yazdırdı
print(result)
