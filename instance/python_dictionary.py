#!/usr/bin/python3
alien_0={'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0={'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position:" +str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3
alien_0['x_position']=alien_0['x_position']+x_increment
print("New x-position:" + str(alien_0['x_position']))

favoriate_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
for name,language in favoriate_languages.items():
	print(name.title() + "'s favoriate language is "+
	language.title() + ".")
#print("Sarah's favorite language is "+
#	favoriate_languages['sarah'].title() +
#	".")

person_new = {
	'first_name':'Zhao',
	'last_name':'caiyun',
	'age':23,
	'city':'Beijing',
	}
for information in person_new.keys():
	print(information+": "+str(person_new[information]))
	
numbers_liked={
	'Bob':23,
	'Eric':34,
	'Tom':22,
	'Groot':32,
	'XiaoBao':1,
	}
for user in numbers_liked.keys():
	print("Hi,is this true about the user's favorite number?")
	print(user+": "+str(numbers_liked[user]))

user_0={
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
	}
for key,value in user_0.items():
	print("\nKey: "+key)
	print("Value: "+value)

