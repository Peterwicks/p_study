# TASK 14: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes input of 2 values and adds them. The program should only accept numbers and floats only or otherwise display an error “invalid character entered” and take the user to re-enter the inputs .
# Once you learn functions,revisit this and write this code inside a function.
# input1 = int(input('Enter a number'))
# input2= int(input('Enter a number'))
# if type(input1) and type(input2) == float or int:
#     output = input1+input2
# else:
#     output = 'invalid character entered” and take the user to re-enter the inputs.'
# print(output)
while True:
    try:
        input1=float(input('Enter first number '))
        input2=float(input('Enter second number '))

        result = input1+input2
        print(result)
        break
    except:
        print('Invalid character entered')
