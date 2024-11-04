# Conditional statement provide a choice for the control flow vbased on a certain condition
# # if conditional statement
# #  it will ony run if the condition is true
# # if condition:
# # If elif else used to check many conditions with different outcomes
# if 20>40:
#     print ('20 is greater')
# else:
#     print('20 is less than ')


# marks = 70
# if marks >50:
#     print ('pass')
# else:
#     print('fail')
#     # declare a variabe number and check if the number is even otherwise display odd
# num = 10
# if num%2==0:
#     print ('even')
# else: 
#     print('odd')
# marks = int(input('enter marks'))
# if marks >=90 and marks <=100:
#     print("A")
# elif marks>=80 and marks<90:
#     print("B")
# elif marks>=70 and marks<80:
#     print("C")
# elif marks>=60 and marks<70:
#     print("dD")
# elif marks>=50 and marks<60:
#     print("E")
# elif marks<=50 and marks>=0:
#     print("fail")
# else:
#     print("Invalid marks")
# Write a program that takes input age frim the user
# If age is 60  or above print you are older
# if age is 18 and above print your an adult
# otherwiae you are a minor
age = int(input("Enter your age"))
if age >=80:
    print ('you are older')
elif age>=18:
    print('you are an adult')
else:
    print ('you are a minor')
# Nested if statements they are if statement inside otherblock
# you give 100discount on purchase above 1000
# you give 200 discount on purchase above 5000
# else no discount
purchase = int(input('enter total purchases'))
if purchase > 1000:
    print('100 discount')
    if purchase>500:
        print('200 discount')
else:
        print('No discount')
# Write a program that takes users age as input
#  If  the age is 18 and above, check if they have drivers license
# if they do have, print your are eligible to drive
# if they dont have licence, print you are not eleigibel to drive
# otherwise print you are too young to drive
