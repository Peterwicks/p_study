person = {
    'name': 'Peter', 
    'Age':26, 
    'gender':"male",
'location':["Kiambu", 518, 'Thika'],
'address':{
    'street':'Muthaiga',
    'City': 'Nairobi', 
    'country': 'Kenya'
}
}
# print(type(person))
# print(person["name"])
# print(person['Age'],person['gender'])
# print(person['location'][1])
# print(person['location'][2])
# print(person['address']['country'])
# print(person['address']['City'])
# print(person['address']['street'])
person['Age']=21
# print(person)
# update location
person['location']= ['Kenya Israel']
# address
person['address']['street']='Donholm'
# Add a new key and value
person['Occupation']= 'Land Surveyor'
# print(person)
# Dictionary methods
# .keys=>returns all the keys
# print(person.keys())
# # .values() returns all the values in the dictionary
# print(person.values())
# .items() returns a list of key and value
# print(person.items())
# .pop() removes element with the specified key
person.pop('Age')
# print(person)
person.pop('Occupation')
# print(person)
# .get() returns the value of a specified key
print(person.get('address'))