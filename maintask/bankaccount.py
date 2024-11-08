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
            return f'deposit amount vannot be less than 0'
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
        