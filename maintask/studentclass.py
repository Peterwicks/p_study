# 1.Create a class called Student with attributes name and age.
# Add a method introduce that prints: "Hello, my name is [name] and I am [age] years old."
class student():
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def introduce(self):
        return f'Hello, my name is {self.name} and I am {self.age} years old'
Details = student("Peter Mutinda",26)
print(Details.introduce())