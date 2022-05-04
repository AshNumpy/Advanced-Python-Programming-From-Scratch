with open("C:/Users/ramaz/OneDrive/Belgeler/GitHub/BTK Python/11-py-file-management/new_file.txt","r+",encoding="utf-8") as file:
    # "r+" read mode can do both read and write
    print(file.read())
    file.write("testing") # "r+" mode provide us to update the file 
    #if we didnt use to "r+" write mode will first clear all content
    # after that update content 
    # but "r+" mode prevent it 
    print(file.read())