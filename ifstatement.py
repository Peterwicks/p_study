# # # Take three inputs from a user, separately. Print the largest of the numbers.
# # #     Hint: Determine what type of data is taken in as input.
num1 = input("Enter your best score 1 " "")
num2 = input("Enter your best score 2" ' 79')
num3= input("Enter your best score 3 ' '")

if num1>num2 and num1>num3:
    print(f"{num1} is the greatest")
elif num2>num1 and num2>num3:
    print(f"{num2} is the greatest")
else:
        print (f"{num3} is the greatest")
# # Take as input from a user the temperature if the temperature is above 30°C display “The temperature is too high”,if the temperature is above 15 display “Normal temperature” otherwise display “Cold temperature”
# # temperature= int(input("Enter your temperature"))
# # if temperature>30:
# #     print("The temperature is too high")
# # elif temperature>15:
# #     print('Normal temperature')
# # else:
# #     print('Cold temperature')
# # Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
# # and if another variable y is greater than 100. If both conditions are true, print "Conditions met", otherwise print "Conditions not met"
x= int(input ('Eneter value of x'))
y= int(input('eneter the value of y'))
if x>=10 and x<=20:
    if y>100:
        print('Conditions met')
# else:
#     print('Conditions not met')
# # 4. Write a Python program that checks if a variable password is equal to the string "secret123". If it is, print "Access   granted", otherwise print "Access denied"
# password = input('Enter Password')
# correct_password= 'secret123'
# if password==correct_password:
#     print('Access granted')
# else:
#     print ('Access Denied')
# . Write a Python program that checks if a variable student_score is greater than 90. If true, check if the attendance is greater than 80. If both conditions are true, print "Excellent student", otherwise print "Good score, but attendance needs improvement"
student_score = int(input ('enter Student score'))
attendance= float(input("enter student's attendance"))
if student_score>90:
    if attendance>80:
        print('Ecellent student')
else:
    print('Good score, but attendance needs improvement')