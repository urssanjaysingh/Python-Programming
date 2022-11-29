# class
class Student:
    # creating method inside class
    # all the attribute that are created from this class will have access to this class
    # while defining method for a class we need to use self as first argument
    # self refers to the object calling it
    def check_pass_fail(self): 
        if self.marks >= 40:
            return True
        else:
            return False

# objects of Student class
student1 = Student()

# adding attribute to student1 object
student1.name = "Harry"
student1.marks = 85

# printing attribute
print(student1.name)
print(student1.marks)

# calling method using student1 object
did_pass = student1.check_pass_fail()
print(did_pass)


student2 = Student()
student2.name = "Janet"
student2.marks = 30
# printing attribute
print(student2.name)
print(student2.marks)
did_pass = student2.check_pass_fail()
print(did_pass)


# python offers a compact way of defining attribute right while instantiating the object
# for that we use the __init__() Method
# the init method is a special method that automatically gets called everytime objects are created
class Student:
    def check_pass_fail(self): 
        if self.marks >= 40:
            return True
        else:
            return False

    def __init__(self, name, marks): # first parameter self refers to object calling it
        self.name = name
        self.marks = marks

# when we create object the __init__() method is called automatically
student1 = Student("Harry", 85)
student2 = Student("Janet", 30)

print(student1.name)
print(student1.marks)
did_pass = student1.check_pass_fail()
print(did_pass)

print(student2.name)
print(student2.marks)
did_pass = student2.check_pass_fail()
print(did_pass)

