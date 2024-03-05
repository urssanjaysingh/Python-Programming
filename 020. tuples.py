# tuple is immutable we can't change elements in tuple
numbers = (21, -5, 6, 9)
print(numbers)

# accessing element
numbers = (21, -5, 6, 9)
print(numbers[2])

# slicing
numbers = (21, -5, 6, 9)
print(numbers[1:4])

# iterating through tuples
numbers = (21, -5, 6, 9)
for number in numbers:
    print(number)