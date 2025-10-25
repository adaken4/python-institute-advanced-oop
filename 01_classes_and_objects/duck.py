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
        return f"Duck({self.sex}, {self.height}m, {self.weight}kg)"

# Object instantiation    
duck = Duck(0.25, 3.6, "female")

# Method invocation
duck.quack()

# Attribute access
print(f"Duck's weight: {duck.weight} kg")

print(duck)