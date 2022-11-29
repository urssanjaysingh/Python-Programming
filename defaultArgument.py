# default value argument
# positional arguments
def add_numbers(n1 = 100, n2 = 1000): 
    sum = n1 + n2
    return sum

result = add_numbers()
print(result)
result = add_numbers(5.4)
print(result)


# passing argument by name 
# known as non-postional or keyword arguments
def greet(name, message):
    print("Hello", name)
    print(message)
    
greet("Jack", "What's going on?")
greet(message = "Howdy?", name = "Jill")
