'''
Logical Operators
and     True if both operands are True
or      True if either of the operands is True
not     True if the operand is False
'''

age = 22
gpa = 3.8
print('')
result = age >= 18 and gpa > 3.6
print(result)
result = age >= 18 and gpa > 3.9
print(result)

print('')
result = age >= 18 or gpa > 3.9
print(result)

print('')
result = True
print(not result)
print('')
age = 14
result = False
print(not age <= 18)
