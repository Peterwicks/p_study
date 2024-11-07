# A class is a blueprint of creating objects
# attributes()variables inside a class
# methods() functions inside a class
# objects are instance of class
# Creating class
# Class Class_name
    # constructor method(used to initialise objects)
    # def _init_(self)
# define a class named car
class Car:
    def __init__(self, color, brand, shape):
        self.color=color
        self.brand=brand
        self.shape=shape
    def describe(self):
        return f'the color of this car is {self.color} and the brand is {self.brand} the shape is {self.shape}'
mycar=Car('red', 'BMW', 'wagon')
print(mycar.describe())
print(mycar.brand)