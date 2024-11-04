# Using Python or PHP or Java or Ruby or JavaScript
# Write a program that lets the user input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. If the password is correct access is granted. After you show them a message , the account is blocked.
# Once you learn functions,revisit this and write this code inside a function.

# correct_password='admin@123'
# attempts = 4
# for i in range(attempts, 0,-1):
#     password = input("Enter password")
#     if password ==correct_password:
#         print("correct password, access granted")
#         break
#     elif i-1>0:
#         print(f'Incorrect password, you have {i-1} attempts left')
#     else:
#         print("Incorrect password account closed")
attempts = 4
correct_password= 'admin@123'
for i in range(attempts):
    password = input("Enter Password")
    if password== correct_password:
        display= 'access granted'
        break
    else:
        remaining_attempts=attempts -(i+1)
        print (f"Incorrect password, you have {remaining_attempts} attempts remaining")
        if remaining_attempts==0:
            display= 'Account blocked'
print(display)

# correct_password = 'admin@123'
# max_attempts = 4
# attempts = 0

# while attempts < max_attempts:
#     password = input('Enter your password ')
#     if password==correct_password:
#         display= 'Access Granted'
#         break
#     else:
#         attempts+=1
#         display = f"Incorrect password, you have {attempts} attaempts remaining "
# if attempts== max_attempts:
#     display ="Account Blocked"
# print(display)