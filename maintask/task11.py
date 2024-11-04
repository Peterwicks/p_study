# # TASK 11: Using Python or PHP or Java or Ruby or JavaScript
# # Write a program that takes the date of birth of a person and the program outputs the age in terms of years,months,days TODAY.
# # Once you learn functions,revisit this and write this code inside a function.
# from datetime import date
# current_date = date.today()
# date_of_birth = (input('Enter your dates of birth YY-MM-DATE '))
# year, month, day = map(int, date_of_birth.split('-'))
# date_of_birth= date(year, month, day)
# Age = current_date-date_of_birth
# if (current_date.month, current_date.day) < (date_of_birth.month, date_of_birth.day):
#     Age -= 1
# print(Age)
from datetime import datetime, date
dob=input('enter date of birth yyyy/mm/dd ')
dob_split= dob.split('-')
today = datetime.now()
today_month= today.month
today_year = today.year
today_day= today.day
years= today_year-int(dob_split[0])
months= today_month-int(dob_split[1])
if int(dob_split[1])>today_month:
    years= years-1 
    months = (today_month+12)-int(dob_split[1])
days= today_day-int(dob_split[2])
if int(dob_split[2])>today_day:
    months = months-1
    days = (today_day+30)-int(dob_split[2])
print(f"{years} years , {months} months {days} days")