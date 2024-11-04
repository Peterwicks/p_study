# TASK 13: Using Python or PHP or Java or Ruby or JavaScript or C# or Go
# Write a program that takes the email and password as input from a user and checks if they are equal to “admin@mail.com” and password is “Admin@123” , if so then print  “Login is Successful” and if not print “Invalid username or password”. ONLY accept 3 tries after which it notifies you that you have been blocked.
# Once you learn functions,revisit this and write this code inside a
correct_email= 'admin@mail.com'
correct_password= 'Admin@123'
attempts = 3
for i in range(attempts+1):
   Email = input("Enter your Email")
   if Email == correct_email:
      Password = input("Enter your password")
      if Password== correct_password:
         Login= ('Log In successful')
print(Login)
     