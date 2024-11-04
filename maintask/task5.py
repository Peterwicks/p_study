# Using Python or PHP or Java or Ruby or JavaScript
# Implement a program that takes 3 users  inputs from the terminal or the Browser, and stores them in three variables. Return the largest of the three. Do this without using the the inbuilt max () function!
# The goal of this exercise is to think about some internals that programs normally take care of for us.
variable1=int(input('Enter the first value')) 
variable2=int(input('Enter the second value')) 
variable3=int(input('Enter the third value')) 
largest_variable=""
if variable1>variable2 and variable1>variable3:
    largest_variable= variable1
elif variable2>variable1 and variable2>variable3:
    largest_variable= variable2
elif variable3>variable1 and variable3>variable2:
    largest_variable=variable3
else:
    largest_variable=(" All are equal")
print(f'the largest variable is {largest_variable}')