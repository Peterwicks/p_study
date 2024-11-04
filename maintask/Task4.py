# Using Python or PHP or Java or Ruby or JavaScript
# Write a program which accepts email as form input or from terminal. Validate the email by checking if it's a valid email. 
# Hint: Check if it contains an “@” symbol and “.” symbol.
# Once you learn functions,revisit this and write this code inside a function.
email=input("Enter your Email")
# if email.count("@")==1 and email.count(".")==1:
#     print('Valid Email')
# else:
#     print("Invalid Email")

# if '@' in email abd "." in email:
#     result = "Valid Email"
# else:
#     result = "Invalid Email"
# print(result)

if email.index("@")>0 and email.index("@")<email.index("."):
    print("Valid Email")
else:
    print('Invalid Email')

# Regular expression(regex)

