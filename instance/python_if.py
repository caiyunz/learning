#!/usr/bin/python3
cars=['audi','bmw','subaru','toyota']
for car in cars:
	if car=='bmw':
		print(car.upper())
	else:
		print(car.title())

car='Audi'
if car.lower()=='audi':
	print("True")
else:
	print("False")

banned_users=['andrew','carolina','david']
user='marie'
if user not in banned_users:
	print(user.title()+",you can post a response if you wish.")
car='subaru'
print("Is car == 'subaru' ? I predict True.")
print(car=='subaru')

print("\nIs car == 'audi' ? I predict False.")
print(car=='audi')

print("Conditional tests:")
print("test"=="Test")
print("test".lower()=="test")
print(2==3)
print(2==2)
print(2<1 or 2<=1)
print(3>2 or 3>=1)
print(3>2 and 2>=4)
print(3>2 and 2<1)

fruits_bad=['banana','apple','pear']
fruit="strawberry"
if fruit in fruits_bad:
	print("This "+fruit+" can't eat!")
else:
	print("This "+fruit+" can eat!")

animal_not=['dog','cat','sheep']
animal="rabbit"
if animal not in animal_not:
	print(animal.title() +" not in the unliked animal list.")

age=17
if age>=18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")
else:
	print("You are too young to vote.")
	print("Please register to vote as soon as you turn 18!")

age=int(input("Please input your age:"))
if age<4:
	print("You are too young,so you can play for free.")
elif age>=4 and age<18:
	print("Please take 5$ for happy.")
elif age>=65:
	print("You can play for half money 5$.")
else:
	print("Please take 10$ for happy.")
