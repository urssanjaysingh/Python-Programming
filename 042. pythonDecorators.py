# Python decorator is a function that takes another function
# add some functionality to it and then return it
def inc(x):
    return x + 1

# decorator function
def operate(func, x):
    result = func(x)
    return result

print(operate(inc, 3))

# function inside another function
def print_msg(message):
    greeting = "Hello"
    
    def printer():
        print(greeting, message)
        
    printer()

print_msg("Python is awesome")

# another way
def print_msg(message):
    greeting = "Hello"
    
    def printer():
        print(greeting, message)
        
    return printer

func = print_msg("Python is awesome")
func()


# DECORATOR
def printer():
    print("Hello world!")
    
def display_info(func):
    
    def inner():
        print("Executing", func.__name__, "function")
        func()
        print("Finished execution")
        
    return inner

decorated_func = display_info(printer)
decorated_func()

# @DECORATOR 
# this code is equivalent to above code
def display_info(func):
    
    def inner():
        print("Executing", func.__name__, "function")
        func()
        print("Finished execution")
        
    return inner

@display_info
def printer():
    print("Hello world!")
    

# decorating function with parameters
def smart_divide(func):
    def inner(a, b):
        print("Dividing", a, "by", b)
        if b == 0:
            print("Cannot divide by 0!")
            return
        return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    return a / b 

value1 = divide(15, 3)
print(value1)

value2 = divide(5, 0)
print(value2)


# chaining decorators in python
def star(func):
    def inner(arg):
        print("*" * 30)
        func(arg)
        print("*" * 30)
    return inner

def percent(func):
    def inner(arg):
        print("%" * 30)
        func(arg)
        print("%" * 30)
    return inner

@star
@percent
def printer(msg):
    print(msg)
    
printer("Decorators are wonderful")