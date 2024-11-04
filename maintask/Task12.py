# TASK 12: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that prints the largest of 4 inputs taken in from a user. Assume that the user would not enter any two numbers which are the same.
# Once you learn functions,revisit this and write this code inside a function.
input_1 = int(input("Enter first number "))
input_2 = int(input("Enter secondnumber "))
input_3 = int(input("Enter third number "))
input_4 = int(input("Enter fourth number "))
if input_1>input_2 and input_1>input_3 and input_1>input_4:
    largest= input_1
elif input_2>input_1 and input_2>input_3 and input_2>input_4:
    largest= input_2
elif input_3>input_1 and input_3>input_2 and input_3>input_4:
    largest= input_3
else:
    largest=input_4
print(f'the largets input is {largest}')
