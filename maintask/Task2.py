# Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
#  Hint: how does an even / odd number react differently when divided by 2?
# Once you learn functions,revisit this and write this code inside a function.
number = int(input("enter a number"))
if number%2==0:
    print ('Even')
    if number%4==0:
        print("Divisible by 4")
else:
    print('Odd')