# we use def keyword to define a function
# always define the function before function calling i.e. above the function call
def greet(): #non argument function
    print("Hello")
    print("How do you do?")
    
# function call
greet()


# argument function
def greet(name): 
    print("Hello", name)
    print("How do you do?")
    
greet("Jack")

# multi arguments
def add_numbers(n1, n2):
    result = n1 + n2
    print("The sum is", result)
    
number1 = 5.4
number2 = 6.7
add_numbers(number1, number2)

# return value from a function
# it is better just to find the addition in function then just return the value
# after return statement the function is imediately terminate and control goes back to function call
def add_numbers(n1, n2):
    result = n1 + n2
    return result

number1 = 5.4
number2 = 6.7
result = add_numbers(number1, number2)
print("The sum is", result)


# finding average marks and grade of a student
# function to find average marks
def find_average_marks(marks):
    total_marks = sum(marks)
    total_subjects = len(marks)
    average = total_marks//total_subjects
    return average

# calculate the grade and return it
def compute_grade(average_marks):
    if average_marks >= 80:
        grade = 'A'
    elif average_marks >= 60:
        grade = 'B'
    elif average_marks >= 50:
        grade = 'C'
    else:
        grade = 'F'
    return grade

marks = [55, 64, 75, 80, 65]
average_marks = find_average_marks(marks)
print("Your average marks is:", average_marks)

grade = compute_grade(average_marks)
print("Your grade is:", grade)
