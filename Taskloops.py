# 1. Write a program that displays a numbers 1 to 50 inside a list.
Numbers = list(range(1,51))
# print (Numbers)
# 2.From 1 above display the ones divisible by 7 or 5 inside a list.
display=[]
for i in Numbers:
    if i%5==0:
        display.append(i)
    elif i%7==0:
        display.append(i)
# print(display)
divisible_seven_5=[]
for num in Numbers:
    if num %7==0 or num%5==0:
        divisible_seven_5.append(num)
print(divisible_seven_5)
# 3. Find sum and average of values in the range between 10 to 40.
Sm= []
for p in (range(10,41)):
    Sm.append(p)
total_sum = sum(Sm)
print(total_sum)
Count = len(Sm)
average=total_sum/Count
print(average)
num = list (range(10,41))
sum = 0
count = 0
for i in num:
    sum+=i
print(sum)
#4.  Put in a list the first 10 odd numbers between 10 to 50.
odd = []
count =0
for x in range(10,50):
    if x%2!=0:
        odd.append(x)
        count+=1
        if count==10:
            break
print(odd)
# print(odd)
# write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
Number = int(input("Enter number: "))
for i in range(11):
    result = Number*i
    print(f"{Number} x {i} = {result}")

# write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
Count = 0
for n in range (1,51):
    if n%2==0:
        Count +=1
print(Count)
# ls1 = [ (“Jay”, 20), (“Mo”, 30), (“Mya”, 32) ]
# Display the total quantity of the 3 above.
total_quantity =0
ls1 = [("Jay", 20), ("Mo", 30), ("Mya", 32) ]
total_quantity=0
for l in ls1:
    stock = l[1]
    total_quantity+=stock
print(total_quantity)
