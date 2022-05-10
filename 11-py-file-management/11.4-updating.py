# with open("suchFile.txt","r+",encoding="utf-8") as file:
#     # "r+" mode is can do both of write and read
#     file.seek(20)
#     file.write("Deneme")


# with open("suchFile.txt","a",encoding="utf-8") as file:
#     # "a" mode is starting end of the page append mode
#     file.write("\n Ramazan Erduran")

#***************Top of Page Update********************#

# with open("suchFile.txt","r+",encoding="utf-8") as file:
#     content = file.read()
#     content = "Before text \n" + content
#     file.seek(0)
#     file.write(content)

#*****************Middle of Page Update*******************#

with open("suchFile.txt","r+",encoding="utf-8") as file:
    list = file.readlines()
    list.insert(1,"Another name insert now \n")
    # set 1st index to "Another name insert now" string
    file.seek(0)
    # for i in list:
    #     file.write(i)
    file.writelines(list) # same as the for loop


with open("suchFile.txt","r",encoding="utf-8") as file:
    print(file.read())