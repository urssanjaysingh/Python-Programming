# in Python, an object which implements the __iter__() method is called an iterable.
numbers = [1, 4, 9]
print(dir(numbers))
value = numbers.__iter__()
print(value)

# Iterator in Python is simply an object that can return data one at a time
# while iterating over it
# for an object to be an iterator, it must implement two methods:
#   iter
#   next
# the __next__() method return the next value in the iteration
# and updates the state to the next value
numbers = [1, 4, 9]
value = numbers.__iter__()
item1 = value.__next__()
print(item1)
item2 = value.__next__()
print(item2)
item3 = value.__next__()
print(item3)

# second way to iter
numbers = [1, 4, 9]
value = iter(numbers)
item1 = next(value)
print(item1)
item2 = next(value)
print(item2)
item3 = next(value)
print(item3)

# working of for loops
num_list = [1, 4, 9]
iter_obj = iter(num_list)
# while loop
while(True):
    try:
        element = next(iter_obj)
        print(element)
    except StopIteration:
        break
# for loop
num_list = [1, 4, 9]
for element in num_list:
    print(element)
    
# creating custom iterator
class Even:
    def __init__(self, max):
        self.n = 2
        self.max = max
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n <= self.max:
            result = self.n
            self.n += 2
            return result
        else:
            raise StopIteration
numbers = Even(10)
print(next(numbers))
print(next(numbers))
print(next(numbers))
