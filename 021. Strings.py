# strings in python are immutable we can't change the string characters

# string with single quotes
text1 = 'Hello'
print(text1)

# string with double quotes
text2 = "You"
print(text2)

# string with multiple line
text3 = """Hello there
How are you doing?""" 
print(text3)

# ESCAPING character backslash(\)
text4 = "He said, \"What\'s there?\""
print(text4)

# accessing character from strings
# string is a sequence of characters
#  0      1       2       3       4       5
# 'P'    'y'     't'     'h'     'o'     'n'
# -6     -5      -4      -3      -2      -1
text = "Python"
print(text[3])
print(text[-4])
# slicing
print(text[1:4])
print(text[:4])
print(text[1:])
