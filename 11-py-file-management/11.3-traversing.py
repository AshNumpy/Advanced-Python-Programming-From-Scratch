
with open ("C:/Users/ramaz/OneDrive/Belgeler/GitHub/BTK Python/11-py-file-management/new_file.txt","r",encoding="utf-8") as file:
    content = file.read(25) 
    print(content)
    print(file.tell()) # location of cursor
    content2 = file.read()
    print(content2)
    file.seek(0) # set cursors locaiton to zero 
    print(file.tell()) # location of cursor
    content3 = file.read()
    print(content3)

# "with" operating like loop 
# when "with" endin otomatically executing "file.close()" code
