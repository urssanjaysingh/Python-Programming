# os module(work with directory)
import os 

# getting current directory
import os
current_dir = os.getcwd()
print(current_dir)

# change the current working directory
import os
os.chdir("C:/Users/Sanjay Singh/Python VS Code/game")
print(os.getcwd())
# testing 
with open("test.txt", "w") as f:
    f.write("This is a test file.")
    
# in Python, all files and sub-directories inside a directory can be retrieved
# using the listdir() function of the os module
import os
print(os.listdir())

# for sub-directories
import os 
print(os.listdir("game"))

# create a new directory using the mkdir() function of the os module.
import os
os.mkdir("game/test")

# rename a directory or file using os.rename() function
# which takes in 2 arguments: old name & new name
import os
os.rename("test", "test-new")

# renaming
import os
os.rename("test-new", "test")

# renaming a file
# first create a file
with open("test.txt", "w") as f:
    f.write("This is a test file.")
# now rename it
import os 
os.rename("test.txt", "testnew.txt")

# changing name back to test.txt
import os 
os.rename("testnew.txt", "test.txt")

# removing a file
import os
print(os.listdir())
os.remove("test.txt")
print(os.listdir())

# remove a directory
# note: directory should be empty
import os
print(os.listdir())
os.rmdir("test")
print(os.listdir())