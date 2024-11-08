# Define a class Calculator with methods add, subtract, multiply, and divide that perform the respective operations on two numbers.
# Create an object of Calculator and use it to perform some calculations.
class calculator():
    def __init__(self, num1, num2):
        self.num1= num1
        self.num2=num2
    def add(self):
        return self.num1+self.num2
    def substarct(self):
        return self.num1-self.num2
    def multiply(self):
        return self.num1*self.num2
    def divide(self):
        return self.num1/self.num2
numbers = calculator(24,6)
print(numbers.divide())
print(numbers.substarct())
print(numbers.add())
print(numbers.multiply())