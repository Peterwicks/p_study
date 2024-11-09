# .Define a class BankAccount with attributes owner and balance (set balance to 0 by default).Add methods deposit and withdraw to modify the balance and a method get_balance to display the balance.
# Ensure that the withdraw method does not allow the balance to go negative.
# class bank_account():
#     def __init__(self, owner, transaction):
#         self.owner= owner
#         self.balance= 0
#         self.transaction=transaction
#     def Deposit(self):
#         return self.balance+self.deposit
#     def Withdrawal(self):
#         if self.withdrawal>self.balance:
#             return "You cannot withdraw, your balance is lower than intended withdrawal"
#         else: 
#             return self.balance-self.withdrawal
#     def get_balance(self):
#         return f'Hello {self.owner}, Your Balance is {self.balance}'
# x = bank_account('Peter', input("Enter your inteneded transaction, withdrawal or deposit").lower, 40000)
# if x == "withdrawal":
#     balance= bank_account.Withdrawal()
# else:
#     balance= bank_account.Deposit()
#     print(balance.get_balance())
class bank_account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            return f'Hello, {self.owner},{amount} deposited, your balance is {self.balance}'
        else:
            return f'deposit amount cannot be less than 0'
    def withdraw(self, amount):
        if amount>self.balance:
            return f'Hello, {self.owner}, Insufficient balance, the maximum amount you can withdraw is {self.balance}'
        else:
            self.balance-=amount
            return f'Hello, {self.owner}, You have withdrawn {amount}, your balance is {self.balance}'
    def get_balance(self):
        return f'Hello, {self.owner}, your current blance is {self.balance}'

person1= bank_account('Peter')
person1.deposit(10000)
person1.withdraw(5000)
print(person1.get_balance())

# Define a class Rectangle with attributes width and height.
# Add methods area and perimeter to calculate the area and perimeter of the rectangle.
# Instantiate a few rectangle objects and print their area and perimeter.
class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height= height
    def area(self):
        return self.width*self.height
    def perimeter(self):
        return 2*(self.width+self.height)
rectangle1= rectangle(40,20)
rectangle2=rectangle(34,20)
rectangle3=rectangle(20,15)
print(f'Area of rectangle 1 is {rectangle1.area()}')
print(f'Perimeter of rectangle 1 is {rectangle1.perimeter()}')
print(f'Area of rectangle 2 is {rectangle2.area()}')
print(f'Perimeter of rectangle 2 is {rectangle2.perimeter()}')
print(f'Area of rectangle 3 is {rectangle3.area()}')
print(f'Perimeter of rectangle 3 is {rectangle3.perimeter()}')
        
# Create a class Employee with attributes name and salary.Add a method give_raise that increases the salary by a given percentage.Instantiate an employee, give them a raise, and display their new salary.
class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary=salary
    def give_raise(self, increase):
            self.salary = self.salary + (increase/100)*self.salary
            return self.salary
    def salaryincreament(self):
        return f'Hello, {self.name}, your new salary is {self.salary}'
employee1= employee("peter", 50000)
employee1.give_raise(10)
print(employee1.salaryincreament())
# Create a base class Vehicle with attributes brand and model.
# Create two subclasses Car and Motorcycle that inherit from Vehicle and add unique methods to each subclass (e.g., honk for Car and rev_engine for Motorcycle).
# Instantiate both subclasses and call their methods.
class vehicle():
    def __init__(self, brand, model):
        self.brand = brand
        self.model= model
class Car(vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    def honk(self):
        return f'The car {self.brand} is model {self.model} '
class Motorcycle(vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    def rev_engine(self):
        return f'The Motocycle {self.brand} is model {self.model}'
Car1= Car('Premio','Toyota')
Motorcycle1= Motorcycle('Yamaha', 'f3')
print(Car1.honk())
print(Motorcycle1.rev_engine())
