#!/usr/bin/python3
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
	print(alien)

aliens = []
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

for alien in aliens[:5]:
	print(alien)
print("...")
print("Total number of aliens: "+str(len(aliens)))

pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
	}
print("You ordered a "+pizza['crust'] + "-crust pizza "+
	"with the following toppings:")
for topping in pizza['toppings']:
	print("\t" + topping)
	
favorite_languages = {
	'jen': ['python','ruby'],
	'sarah': ['c'],
	'edward': ['ruby','go'],
	'phil': ['python','haskell'],
	}
for name,languages in favorite_languages.items():
	print("\n" +name.title() + "'s favorite languages are:")
	for language in languages:
		print("\t" +language.title())
		
user_1={'first_name':'Zhao','last_name':'Caiyun','age':27,'city':'Beijing'}
user_2={'first_name':'Wang','last_name':'Groot','age':27,'city':'Beijing'}
user_3={'first_name':'Wang','last_name':'xiaobao','age':1,'city':'Pingyao'}
peoples=[user_1,user_2,user_3]
for people in peoples:
	print("People's full name is:"+people['first_name']+people['last_name'])
	print("People's age is:"+str(people['age'])+" and live city is:"+people['city'])
	
favorite_places={'groot':['New York','Sinapore','Taland'],'caiyunz':['Tailand','Hongkong','Xianggang'],'xiaobao':['beijing','shijiazhuang','pingyao']}
for name,places in favorite_places.items():
	print("The people's name is:"+name)
	for place in places:
		print("\twanted to go:"+place)
		
cities={'beijing':{'country':'China','population':10,'fact':'GuGong'},'pingyao':{'country':'China','population':5,'fact':'PingYaoGuCheng'},'yuci':{'country':'China','population':7,'fact':'yucioldcity'}}
for name,city_info in cities.items():
	print("The city's name is:"+name)
	for a,b in city_info.items():
		print("\t"+a+"\t"+str(b)+"\t")
