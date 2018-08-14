#!/sur/bin/python3

import os, sys

# Get the path from keyboard
path = ""
prefix = "" #prefix for new files' names
newname = ""

path = input("Please input the path:")
print ("Your path is:", path)
prefix = input("Please give a prefix for your files:")


# Get all files from the path
dirs = os.listdir(path)

#for file in dirs:
#    print (file)

counter = len(dirs) #Files number
n = 0

print(counter)
os.chdir(path)

while n < counter:
    newname = prefix + str(n)
    os.rename(dirs[n], newname)
    n += 1