#****************** .read() ******************
# "r": read. Occuring the error if there isn't file.
file = open("new_file.txt","r", encoding='utf-8')

"""
# for i in file:
#     print(i, end = "") #  end="" usage for end of the lines dont add new line
# print('-'*30)

content1 = file.read()
print('1st content:')
print(content1)

content2 = file.read() # You recognize to there isn't 2nd content 
print('2nd content:') # After you read all of content once, there is no more content in the file. Thats the reason of this situation
print(content2)
file.close()

# But if u first close the file than try to read 
# u will accomplish
file = open("C:/Users/ramaz/OneDrive/Belgeler/GitHub/BTK Python/11-py-file-management/new_file.txt","r", encoding='utf-8')
content2 = file.read()
print('Another try:')
print(content2)
file.close()

file = open("C:/Users/ramaz/OneDrive/Belgeler/GitHub/BTK Python/11-py-file-management/new_file.txt","r", encoding='utf-8')
content3 = file.read(7) # content3 will read only 7 case
print(content3)
"""

#****************** .readline() ******************
"""
print(file.readline(), end="") # read only one line
print(file.readline(), end="")
"""

#****************** .readlines() *****************
liste = file.readlines() # set a list to every line of file
print(liste)
print(liste[2])

file.close()