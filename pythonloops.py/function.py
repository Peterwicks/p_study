# A function is a block of code that performs a specific task and can only run when it is called
# Takes in some data
# performs some operation on the data
# Returns an output
# Creting functions
# Define the function
# give it an name
# def name ():
# block of code

# A function to calculate the area of a triangle
def triangle_area(base, height):
    area=base*height*0.5
    return area
triangle_area(30, 42)
# Create a function thaat calculates the area of a rectangle
def area_Rectangle():
    length= 40
    width=35
    area = length*width
    return area
area_Rectangle()
# Parameters
# Variables that are only used inisde the functions
# Arguements
# Exact values passed when when calling a function
def area_rect(len, width):
    area = len*width
    return  area
area_rect(56,18)
# Write a function that is goig to check is a number is even or odd
def even_odd(number):
    if number%2==0:
        result= "even"
    else:
        result= "odd"
    return result
user_input = int(input("Enter a number"))
x = even_odd(user_input)
print(x)
# TASK 12: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that prints the largest of 4 inputs taken in from a user. Assume that the user would not enter any two numbers which are the same.
# Once you learn functions,revisit this and write this code inside a function.
def largest_input(input1, input2, input3, input4):
    if input1>input2 and input1>input3 and input1>input4:
        largest= f"{input1} is the largest input"
    elif input2>input1 and input2>input3 and input2>input4:
        largest=f"{input2} is the largest input"
    elif input3>input1 and input3>input2 and input3>input4:
        largest=f"{input3} is the largest input"
    else:
        largest= f"{input4} is the largest input"
    return largest
user_input1= int(input('Enter first number'))
user_input2= int(input('Enter second number'))
user_input3= int(input('Enter third number'))
user_input4= int(input('Enter fourth number'))
value = largest_input(user_input1, user_input2, user_input3, user_input4)
print (value)

