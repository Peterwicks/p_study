# Write a program that:
# Takes a transaction amount and account type ("Standard" or "Premium") as input.
# If the account type is "Standard":
# Check if the amount is above 500:
# If it is, print "Transaction exceeds the limit for Standard accounts."
# If not, print "Transaction approved."
# If the account type is "Premium":
# Check if the amount is above 1,000:
# If it is, print "Transaction exceeds the limit for Premium accounts."
# # If not, print "Transaction approved."
# amount=float(input('enter amount'))
# account_type=input('Enter account type')
marks=int(input("Enter your marks: "))
if marks>=0 and marks<=100:
    if marks >=90 and marks <= 100:
        print("You scored an A")
    elif marks >=80 and marks <90:
        print("You scored a B")
    elif marks >=70 and marks <80:
        print("You scored a C")
    elif marks >=60 and marks <70:
        print("You scored a D")
    elif marks >=50 and marks <60:
        print("You scored an E")
    else:
        print("You failed!")
else:
    print("Invalid marks")
