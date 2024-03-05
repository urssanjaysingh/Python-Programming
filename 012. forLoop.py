# Sequence: A sequence in python is a collection of items in an order.
# NOTE: in python while using index with range() or slicing list/tuple
# the first index is inclusive and last is exclusive

text = "Python"
for character in text:
    print(character)

# for loop with list
languages = ["English", "French", "German"]
for language in languages:
    print(language)
    
# for with range() 
for count in range(1, 6): #here 1 is inclusive and 6 is exclusive
    print(count)
    
# multiplication table
number = int(input("Enter an integer: "))
for count in range(1, 11):
    product = number * count
    print(number, "x", count, "=", product)
    count = count + 1