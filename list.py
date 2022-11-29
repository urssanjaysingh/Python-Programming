# list are mutable we can change items in it

# a list of integers
numbers = [1, 5, 6, -4]
print(numbers)

# mixed list
random_list = [2.5, "Hello", -5, 2.5]
print(random_list)

# empty list
list1 = []
print(list1)
print("The size of empty list:", len(list1))

# a list of strings
# index         0           1           2       3
# negative index:
#              -4          -3          -3      -1
languages = ["Python", "JavaScript", "C++", "Kotlin"]
print(languages)
# acessing elements
print(languages[0])
print(languages[2])
print(languages[-1])
print(languages[-3])


# SLICING IN LISTS
# index         0           1           2       3
# negative index:
#              -4          -3          -3      -1
languages = ["Python", "JavaScript", "C++", "Kotlin"]
print(languages[0:3])
print(languages[:3]) 
print(languages[1:4])
print(languages[1:])

# ITERATING
languages = ["English", "French", "German"]
for language in languages:
    print(language)


# CHANGE ITEMS OF A LIST
# index         0           1           2       3
# negative index:
#              -4          -3          -3      -1
languages = ["Python", "JavaScript", "C++", "Kotlin"]
languages[1] = "Ruby"
print(languages)
# changing multiple items
languages[1:3] = ["Ruby", "Dart"]
print(languages)


# NOTE: The in keyword is used to check whether the item is present in the list or not

# index         0           1           2       3
# negative index:
#              -4          -3          -3      -1
languages = ["Python", "JavaScript", "C++", "Kotlin"]
print("Python" in languages)
print("Rust" in languages)

