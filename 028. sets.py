# SETS:
#       items of a set are not in order
#       no duplicate items are allowed
#       items must be immutable objects

# NOTE: Set items are immutable but sets are mutable;
#       we can add and remove items from a set

animals = {"dog", "cat", "tiger", "elephant"}
print(animals)

# converting a list into set
animals = set(["dog", "cat", "tiger", "elephant"])
print(animals)

# add items into set
animals = {"dog", "cat", "tiger", "elephant"}
animals.add("monkey")
print(animals)

# adding sequence(list, tuple) into set
animals = {"dog", "cat", "elephant"}
wild_animals = ["tiger", "leopard", "elephant"]
animals.update(wild_animals)
print(animals)

# we can pass multiple iterable in update()
animals = {"dog", "cat", "elephant"}
wild_animals = ["tiger", "leopard"]
animals.update(wild_animals, {"dolphins"})
print(animals)

# remove items from a set using discard()
animals = {"dog", "cat", "elephant"}
animals.discard("dog")
print(animals)

# difference between discard() and remove()

# discard()
animals = {"dog", "cat", "elephant"}
animals.discard("ferret") #it will not throw an error
print(animals)

# remove()
animals = {"dog", "cat", "elephant"}
animals.remove("ferret") #it will throw an error
print(animals)

# clear()
animals = {"dog", "cat", "elephant"}
animals.clear()
print(animals)


# SET OPERATIONS

# union
domestic_animals = {"dog", "cat", "elephant"}
wild_animals = {"lion", "tiger", "elephant"}
# animals = domestic_animals.union(wild_animals)
animals = domestic_animals | wild_animals
print(animals)

# intersection
domestic_animals = {"dog", "cat", "elephant"}
wild_animals = {"lion", "tiger", "elephant"}
# animals = domestic_animals.intersection(wild_animals)
animals = domestic_animals & wild_animals
print(animals)