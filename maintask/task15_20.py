# TASK 15: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes input of someone's basic salary and benefits, adds them to fin
# d the gross salary then uses  the gross salary to find the NHIF. 
# To find the Kenya NHIF Rate using THIS LINK:  
# Write a normal program but use functions if you feel comfortable.
def calc_Gross_Salary(BS,B):
    gross_salary= BS+B
    return gross_salary
basic_salary=float(input('Enter your basic salery '))
benefits= float(input('Enter you benefits '))
Gross_salary=calc_Gross_Salary(basic_salary,benefits)
print(f'your gross salary is {Gross_salary}')
# uses  the gross salary to find the NHIF. 
def calc_NHIF(G):
    if G<=5999:
        nhif=150
    elif G >5999 and G<=7999:
        nhif=300
    elif G >7999 and G<=11999:
        nhif=400
    elif G >11999 and G<=14999:
        nhif=500
    elif G >14999 and G<=19999:
        nhif=600
    elif G >19999 and G<=24999:
        nhif=750
    elif G >24999 and G<=29999:
        nhif=850
    elif G >29999 and G<=34999:
        nhif=900
    elif G >34999 and G<=39999:
        nhif=950
    elif G >39999 and G<=44999:
        nhif=1000
    elif G >44999 and G<=49999:
        nhif=1100
    elif G >49999 and G<=59999:
        nhif=1200
    elif G >59999 and G<=69999:
        nhif=1300
    elif G >69999 and G<=79999:
        nhif=1400
    elif G >79999 and G<=89999:
        nhif=1500
    elif G >89999 and G<=99999:
        nhif=1600
    else:
        nhif=1700
    return nhif
NHIF=calc_NHIF(Gross_salary)
print(f'Your NHIF contribution is {NHIF}')
# TASK 16: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the program above, then use  the gross salary to find the NSSF. 
# To find the Kenya NSSF Rate  using 6% of the Gross Salary. BUT ONLY A MINIMUM OF 18,000 Gross Salary CAN BE USED IN NSSF. 
def calc_NSSF(GS):
    if GS>=0 and GS<18000:
        nssf=0.6*GS
    else:
        nssf=0.6*18000
    return(nssf)
NSSF= calc_NSSF(Gross_salary)
print(f'Your NSSF contributiob is {NSSF}')

# Task 17: Using Python or PHP or Java or Ruby or JavaScript
# Continue with the same program and calculate an individual’s NHDF using:
#  i.e NHDF = gross_salary *  0.015
def calc_NHDF(gs):
    nhdf=gs*0.015
    return(nhdf)
NHDF=calc_NHDF(Gross_salary)
print(f'Your NHDF contribution is {NHDF}')