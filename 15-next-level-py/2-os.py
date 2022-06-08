import os

result = os.name # windows -> nt
result = os.getcwd() # dir folder

# FOLDER CREATING
# os.chdir('../..') # go upper file
# os.mkdir('newdirectory') # new file to .getcwd() location

# LISTING
result = os.listdir()
print(result,'\n')

for file in os.listdir():
    if file.endswith('.txt'):
        print(file)

