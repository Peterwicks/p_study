# Clean up the following variable to give the clean version in lower case. Using inbuilt methods in the str class 
name = "  JOHn  ."
# name = name.strip().replace('.,', '')
# print(name.lower())
# change to lower case
name = name.lower()
# clean 
name = name.strip()
# replace
name = name.replace(".", "")
print(name)


# Slice the below string to get you the resulting sentence:
sentence_one ="The Dog Breed is German Shepherd"
print(sentence_one[8:23])
# only display “Breed is German"
sentence_two = "Defeats for the Clinton forces, this was her moment of triumph"
# only display “Clinton forces”
print(sentence_two[16:30])

# Split the below sentence using a semicolon i.e ; And display length of the result. 
sentence = "The lazy dog; ran so fast; it hit the wall. "
sentence3= sentence.split("; ")
print(sentence3.__len__())

first_name="  Joh.n"  
last_name="   Do,e" 
first_name1= first_name.replace('.', '').strip()
last_name1= last_name.replace(',', '').strip()
fullname = first_name1 +' ' +last_name1
print(fullname)
# Clean up and display Full name i.e John Doe

# having the string r = '["E","W","C"]' #Manipulate it to display EWC
r = '["E","W","C"]'
r2=''.join(filter(str.isalpha,r))
print (r2)

# Attempt questions in the link below. Whether you get the right answer or not, still read the solution explanation.
# https://realpython.com/quizzes/python-strings/cls
