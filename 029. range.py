# NOTE: range() only works with integers

result = range(1, 11)
print(result)

# convert the result to a list
result = range(1, 11)
print(list(result))

# range() in for loop
for value in range(1, 6):
    print(value, "iteration")
    
# if the start parameter is not passed in range() 
# then default start paremeter will be 0
result = range(11)
print(list(result))

# range with step parameter
result = range(1, 11)
# here by default step 1 is used as third parameter in range()
#  i.e. range(1, 11, 1)
print(list(result))

# with step parameter
result = range(1, 11, 3)
print(list(result))

# we're converting result to list
result = list(range(5, -6, -1))
print(result)