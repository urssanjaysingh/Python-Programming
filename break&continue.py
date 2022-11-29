# break
for item in range(1, 6):
    if item == 3:
        break
    print(item)
print("The end")

while True:
    number = float(input("Enter a number: "))
    if number < 0:
        break
    print("You entered: ", number)

# continue
for i in range(5):
    number = float(input("Enter a number: "))
    if number < 0:
        continue
    print(number)
