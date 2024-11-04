# TASK 13: Using Python or PHP or Java or Ruby or JavaScript or C# or Go
# Write a program that takes the email and password as input from a user and checks if they are equal to “admin@mail.com” and password is “Admin@123” , if so then print  “Login is Successful” and if not print “Invalid username or password”. ONLY accept 3 tries after which it notifies you that you have been blocked.
# Once you learn functions,revisit this and write this code inside a
correct_email= 'admin@mail.com'
correct_password= 'Admin@123'
attempts = 3
for i in range(attempts):
   Email = input("Enter your Email ")
   Password = input("Enter your password")
   if Email == correct_email and Password == correct_password:
      output = ('Login successful')
      break
   else:
      remaining_attempts = attempts -(i+1)
      if remaining_attempts>0:
         output=f'Incorrect Password, you have {remaining_attempts} reamaing'
      else:
         output= "Account Blocked"
   print(output)
     