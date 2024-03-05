# index         0           1           2       3
# negative index:
#              -4          -3          -3      -1
languages = ["Python", "JavaScript", "C++", "Kotlin"]

# adding element at the end
languages = ["Python", "JavaScript", "C++", "Kotlin"]
languages.append("Rust")
print(languages)

# removing particular element by value
languages = ["Python", "JavaScript", "C++", "Kotlin"]
languages.remove("C++")
print(languages)

# adding element at specific position
languages = ["Python", "JavaScript", "C++", "Kotlin"]
languages.insert(1, "Rust")
print(languages)

# copy a list
languages = ["Python", "JavaScript", "C++", "Kotlin"]
languages1 = languages.copy()
print(languages)
