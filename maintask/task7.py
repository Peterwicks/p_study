# Using Python or PHP or Java or Ruby or JavaScript
# Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
# A > 79 , B - 60 to 79, C  > 49 to 59, D - 40 to 49, E - less 40
# Once you learn functions,revisit this and write this code inside a function.
Marks = int(input("Enter Student's Marks "))
Grade = ""
if Marks>=0 and Marks<=100:
    if Marks>79:
        Grade = "A"
    elif Marks >=60 and Marks <=79:
        Grade="B"
    elif Marks >=49 and Marks <60:
        Grade="C"
    elif Marks >=40 and Marks <50:
        Grade="D"
    else:
        Grade = "E"
else:
    Grade = 'The marks you entered are Invalid'
print(f"Student's grade is {Grade}")