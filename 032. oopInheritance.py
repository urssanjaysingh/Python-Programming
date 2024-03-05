# Inheritance allows us to inherit attributes and methods
# from a parent class to child classes

# base/parent class
class Animal:
    def eat(self):
        print("I can eat")

# derived class
class Dog(Animal):
    def bark(self):
        print("I can bark")
        
class Cat(Animal):
    def get_grumpy(self):
        print("I am getting grumpy")
    
dog1 = Dog()
# method of derived class
dog1.bark()
# method of base class
dog1.eat()

cat1 = Cat()
cat1.eat()


# base class
class Polygon:
    def __init__(self, sides):
        self.sides = sides
        
    def display_info(self):
        print("A polygon is a two dimensional shape with straight lines")
        
    def get_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter
    
class Triangle(Polygon):
    def display_info(self):
        print("A triangle is a polygon with 3 edges")
        # if we need we can call the display_info() method of the parent class as follows
    
        # Polygon.display_info(self)
        
        # since we're calling the method using the class rather than object
        # we need to pass self explicitly
        
        # We can use super() function for same then we don't need to pass self
        
        # super().display_info()
        
class Quadrilateral(Polygon):
    def display_info(self):
        print("A quadrilateral is a polygon with 4 edges")
        
t1 = Triangle([5, 6, 7])
perimeter = t1.get_perimeter()
print("The perimeter is", perimeter)

# if the same method is defined in both base and derived classes,
# then the method of the derived class overrides the method of the base class
# this is called METHOD OVERRIDING
t1.display_info()