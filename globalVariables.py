# Note: try to avoid using global varible
# global variable
message = "How you doing?"

def greet():
    # global variable
    message = "How are you?"
    print("Message inside function:", message)
    
greet()
print("Message outside function:", message)


# changing global varible
# we can change global variable by global keyword inside the function
message = "How you doing?"

def greet():
    global message
    message = "How are you?"
    print("Message inside function:", message)
    
greet()
print("Message outside function:", message)