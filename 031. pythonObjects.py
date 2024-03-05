# Everything in Python is an object and we can check this
# using type() function
numbers = [1, 4, 9, 16]
print(type(numbers))

n1 = 5
print(type(n1))

flag = True
print(type(flag))

def my_function():
    pass
print(type(my_function))


# we can list out all the attributes and methods of a given object
# by using the dir() function
numbers_list = [1, 2]
print(dir(numbers_list))

# adding __add__ mehod
numbers_list = [1, 2]
result = numbers_list.__add__([3, 4])
# the + operator internally call this __add__ method when working with list
# thats why we can use the operator like this 
# result = numbers_list + [3, 4]
print(result)


# In Python, every object has an id for identity. 
# The id of an object is always unique and constant for this object during its lifetime.
# we can check the id of a fuction 
# by using id() function
number1 = 5
print(id(number1))

number2 = 10
print(id(number2))
number3 = number2
print(id(number3))

# how variable works
a = [1, 2, 3]
b = a # here a and b refering to the same object
a.append(4)
# output will be same
print("a =", a)
print("b =", b)

a = [1, 2, 3]
b = a.copy() # we can use copy() method to avoid this type of reffering
a.append(4)
# now output will be different
print("a =", a)
print("b =", b)
