class student():
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def introduce(self):
        return f'Hello, y name is {self.name} and I am {self.age} years old'
Details = student("Peter Mutinda","25")
print(Details.introduce())