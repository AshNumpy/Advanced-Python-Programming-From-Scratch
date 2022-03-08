#RAGE
"""for i in range(2,10,2):     # 2'den 10'a kadar 2'şer 10 dahil değil
    print(i)

print(list(range(5,100,10)))
"""


#ENUMERATE:
greeting = 'hello there'

"""index = 0
for i in greeting:
    print(f'index: {index} letter: {i}')
    index +=1
"""

# for i in enumerate(greeting):
#     print(i)

"""
for index,item in enumerate(greeting):
    print(f"index: {index} letter: {item}")"""



#ZİP
list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
list3 = [11,22,33,44,55]
print(list(zip(list1,list2,list3)))
