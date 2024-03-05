# opening a file
# MODE:
# r(Read Mode):opens a file for reading(dafault)
# w(Write Mode):open a file for writing
#               creates a new file if doesn't exist
#               clears the content of the file if it exists
# a(Append Mode):opens a file for appending at the end of the file
#                creates a new file if it doesn't exist.

# reading mode
f = open("message.txt", "r")
# reading from file
content = f.read()
print(content)
f.close()

# read only certain numbers of characters
f = open("message.txt", "r")
content = f.read(6)
print(content)
more_content = f.read(12)
print(more_content)
f.close()

# Exception handling with files
try:
    f = open("message.txt", "r")
    content = f.read(6)
    print(content)
    more_content = f.read(12)
    print(more_content)
finally: # even if our program encountered errors our file will be close
    f.close()    
    
    
# automatically close a file by following method
with open("message.txt", "r") as f:
    content = f.read(6)
    print(content)
    more_content = f.read(12)
    print(more_content)
    

# writing file
with open("python.txt", "w") as f:
    f.write("Python is awesome\n")
    f.write("I love Python")
    

# appending to a file
with open("python.txt", "a") as f:
    f.write("\nPython is my favorite programming language")
    

# readlines() and writelines()
# the readlines() method returns a list containing each of the file.
with open("python.txt", "r") as f:
    lines = f.readlines()
    print(lines)
# the writelines() method writes the items of a list to the file
with open("javascript.txt", "w") as f:
    lines = ["JS is also awesome", "\nJS is my second favorite programming language"]
    f.writelines(lines)