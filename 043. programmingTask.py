# operators
language = "Python"
print("1.", language == "python")

age = 18
print("2.", age >= 18)
print("3.", age > 18)
print("4.", age >= 18 and language == "Java")


# positive or negative
number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is 0")
    
    
# sum of numbers from 1 to 100
sum = 0
for i in range(1, 101):
    sum = sum + i
    result = sum
    i = i + 1
print(result)


# continue
languages = ["Python", "Java", "Swift", "C", "C++"]
for language in languages:
    if language == "Swift" or language == "C++":
        continue
    print(language)
    

# function

def add_numbers(num1, num2):
    result = num1 + num2
    return result
    
def multiply_numbers(num1, num2):
    result = num1 * num2
    return result

num1 = 5.4
num2 = 7.6
addition = add_numbers(num1, num2)
multiplication = multiply_numbers(num1, num2)
print("Addition is:", addition)
print("Multiplication is:", multiplication)


# list & tuple
mixed_list = ["Hello", -34, "Java", True]
print("1.", mixed_list[-1])
mixed_list[1] = "Hi"
print("2.", mixed_list)

mixed_tuple = (1, 3, 4, 5)
mixed_tuple[1] = 100        
print("3.", mixed_tuple)

# Strigs
quote = "Talk is cheap, Show me the code."
print("1.", quote[3])
print("2.", quote[-3])
print("3.", quote.replace("code", "program"))

# dictionary
synonyms = {"mountain":"peak", "forest":"jungle"}
print("1.", synonyms["mountain"])

synonyms["terrain"] = "land"
print("2.", synonyms)

synonyms.pop("forest")
print("3.", synonyms)

# SETS
animals = {"dog", "cat", "tiger", "elephant", "dog"}
print("1.", animals)

animals.remove("cat")
animals.remove("dog")
print("2.", animals)

animals.add("snake")
print("3.", animals)

result = {1, 5, 10} & {100, 10, 3, 5}
print("4.", result)


# range
list_series = list(range(3, 31, 3))
print(list_series)


# OOP-Class
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def peri(self, a, b, c):
        perimeter = a + b + c
        return perimeter

t1 = Triangle(3, 4, 5)
result = t1.peri(3, 4, 5)
print(result)

# Generators
def generate_odd():
    n = 1
    while True:
        yield n
        n += 2

seq = generate_odd()
i = 1 
while i <= 10:
    print(next(seq))
    i += 1