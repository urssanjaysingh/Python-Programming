# Exception handling is the process of responding to exceptions
# in a custom way during execution of a program

# ZeroDivisionError
numerator = 10
denominator = 0
print(numerator / denominator)


# Handling error with try...except
try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    result = numerator / denominator
    print(result)
except:
    # code to run when exception occurs
    print("Denominator cannot be zero, Try again.")

print("Program ends.")


# handling specific exception
try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    result = numerator / denominator
    print(result)
    
    my_list = [1, 2, 3]
    i = int(input("Enter index: "))
    print(my_list[i])
    
except ZeroDivisionError:
    # this handle only ZeroDivisionError
    print("Denominator cannot be zero, Try again.")

except IndexError:
    print("Index cannot be greater than size of list")

print("Program ends.")


# try...finally
try:
    print(1/0)
except:
    print("Wrong denominator")
finally:
    print("Always printed")
    