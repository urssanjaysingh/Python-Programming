# taking user input
# input() always takes input in the string format
# to convert string to an integer we use int()
# to convert string to a float we use float()
name = input("Enter name: ")
print(name)

# type of value
print("")
number1 = 5
print(number1)
print(type(number1))

number2 = 5.5
print(number2)
print(type(number2))
print("")

number = input("Enter number: ")
print("Before Converting...")
print(number)
print(type(number))
number = int(number)
print("After Converting...")
print(type(number))

print("")
# converting input in one line
num = int(input("Enter number: "))
print(num)
print(type(num))
print("")

floatNum = float(input("Enter number: "))
print(floatNum)
print(type(floatNum))