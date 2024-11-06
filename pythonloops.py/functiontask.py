maths= int(input("Enter Maths Marks "))
en=maths= int(input("Enter English Marks "))
swa= int(input("Enter Swahili Marks "))
sci= maths= int(input("Enter Science Marks "))
sos= int(input("Enter Social studies Marks "))
def cal_total_marks(m,e,s,sc,so):
    Sum=m+e+s+sc+so
    return Sum
total_marks=cal_total_marks(maths,en,swa,sci,sos)
print(f'total marks is {total_marks}')

def calculate_average(total):
    average=total/5
    return average
avg= calculate_average(total_marks)
print (f'Average is {avg}')

def find_grade(b):
    if b > 79:
        grade = 'A'
    elif 60 <= b <= 79:
        grade = 'B'
    elif 49 <= b <= 59:
        grade = 'C'
    elif 40 <= b <= 49:
        grade = 'D'
    else:
        grade = 'E'
    return grade
Grade=find_grade(avg)
print(f'Your grade is {Grade}')
    