# A class is blueprint or recipe for an instance.

# Inheritance allows you to get a more specialized
# class based on another class (superclass).

# Your classes could be used as superclasses for
# newly derived classes (subclasses).

# Class Duck definition
class Duck:
    # Instance attributes
    def __init__(self, height, weight, sex):
        self.height = height
        self.weight = weight
        self.sex = sex

    def walk(self):
        pass

    # Method
    def quack(self):
        return print('Quack')
    
    def __str__(self):
        return f"Duck({self.sex}, {self.height}cm, {self.weight}kg)"

# An instance is one particular physical instantiation
# of a class that occupies memory and has data elements.
# Each instance has its own individual state.

# Object instantiation    
duck = Duck(25, 3.6, "female")
duckling = Duck(height=10, weight=3.4, sex="male")
hen = Duck(20, 3.4, sex="female")

# An attribute refers to two major kinds of class traits:
# - variables: holding data about the class or an instance
# - methods: represent a behavior

# Method invocation
duck.quack()

# Attribute access
print(f"Duck's weight: {duck.weight} kg")

print(duck)