# A MODULE is a file contain python code that we can use in our program
import math

number = 25
result = math.sqrt(number)
print(result)

print(math.pi)

# renaming modules
import math as m 
number = 25
result = m.sqrt(number)
print(result)

print(m.pi)

# importing specifically by using 
# from...import statement
from math import sqrt
num = sqrt(64)
print(num)

# importing more than one
from math import pi, sin, sqrt

value = sin(pi/2)
print(value)

num = sqrt(64)
print(num)

# importing all
from math import *

value = sin(pi/2)
print(value)

num = sqrt(64)
print(num)