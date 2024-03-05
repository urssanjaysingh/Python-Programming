# counting
count = 1
while count <= 5:
    print(count)
    count = count + 1;

# multiplication table
number = int(input("Enter a number: ")) 
count = 1
while count <= 10:
    product = number * count
    print(number, "x", count, "=", product)
    count = count + 1
    
# reverse multiplication table
number = int(input("Enter a number: "))
count = 10
while count >= 1:
    product = number * count
    print(number, "*", count, "=", product)
    count = count - 1