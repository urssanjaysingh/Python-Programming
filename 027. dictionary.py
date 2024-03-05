# Dictionary is a collection of key-value pair
# keys are use as indices for accessing, changing elements
#              key   value    key  value
# person1 = {"name":"Linus", "age":21}
#                item1         item2

person1 = {"name":"Linus", "age":21}
print(person1)

# both the keys i.e. 10 & ("age") are immutable objects
person1 = {10: "Linus", ("age"): 21}
print(person1)

# access dictionary elements
person1 = {"name":"Linus", "age":21}
print(person1["name"])

# find whether key exist in dictionary or not by get() method
person1 = {"name":"Linus", "age":21}
print(person1.get("age"))
print(person1.get("hobbies"))
# providing a default value in get() method
person1 = {"name": "Linus", "age": 21}
print(person1.get("hobbies", ["dancing", "fishing"]))

# add/change dictionary elements
person1 = {"name":"Linus", "age":21}
person1["name"] = "Dennis"
print(person1)

# adding new key-value pair
person1 = {"name":"Linus", "age":21}
person1["hobbies"] = ["dancing", "fishing"]
print(person1)

# remove element from a dictionary by pop() method
person1 = {"name":"Linus", "age":21}
print(person1.pop("name"))
print(person1)

# iterating through dictionaries
person1 = {"name":"Linus", "age":21}
for key in person1:
    print(key)
    print(person1[key])