# open() -> open file or create file
# open(file_name, file_access_mode)
# file_access_mode -> specify to which purpose to open file 

# "w": write mode. Creating the file to location.
#   ** This mode delete the file content and replpace new content.
"""
file = open("newFile.txt","w")
file.close() # if u dont need to file anymore, u should close file for ram usage
"""

"""
file = open("C:/Users/ramaz/OneDrive/Belgeler/GitHub/BTK Python/11-py-file-management/new_file.txt","w", encoding='utf-8')
# encoding = 'utf-8' for recognize more case such as turksih cases
file.write("Ayşegül")
file.close()

"""

# "a": append. Create file if there is not.
"""
file = open("C:/Users/ramaz/OneDrive/Belgeler/GitHub/BTK Python/11-py-file-management/new_file.txt","a", encoding='utf-8')
file.write("\nAyşegül ")
file.close()

"""
# "x": create. Occuring the error if there is file already exist.
try:
    file = open("new_file.txt","x", encoding='utf-8')
except Exception as ex:
    print(ex)
