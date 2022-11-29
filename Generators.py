# in generator we use yield keyword to get the next item of the iterator
def even_generator():
    n = 0
    
    n += 2
    yield n
    
    n += 2
    yield n
    
    n += 2
    yield n

numbers = even_generator()
print(next(numbers))
print(next(numbers))
print(next(numbers))


# second way
def even_generator(max):
    n = 2
    
    while n <= max:
        yield n
        n += 2

numbers = even_generator(4)
print(next(numbers))
print(next(numbers))
print(next(numbers))

# infinite stream of data with generators
def generate_fibonacci():
    n1 = 0
    n2 = 1
    while True:
        yield n1
        n1, n2 = n2, n1 + n2

seq = generate_fibonacci()

print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
