#!/usr/bin/python3
pizzias=['ChicagoStyle','CaliforniaStyle','NewYorkStyle','PanPizza']
for pizza in pizzias:
	print(pizza)
	print("I like pepperoni pizza!\n")
print("I really love pizza!")

numbers=list(range(5))
print(numbers)

for i in range(1,8,2):
	print(i)

even_numbers=list(range(1,8,2))
print(even_numbers)

numbers=list(range(1,11))
print(numbers)
for i in range(len(numbers)):
	numbers[i]=numbers[i]**2
print(numbers)

new_numbers=[]
for i in range(1,11):
	new_numbers.append(i**2)
print(new_numbers)

numbers=list(range(10))
print(numbers)
print(max(numbers))
print(min(numbers))
print(sum(numbers))

squares=[value**2 for value in range(1,11)]
print(squares)

number_20=[number for number in range(1,21)]
print(number_20)

numbers_100millon=list(range(1,1000001))
print(max(numbers_100millon))
print(min(numbers_100millon))
print(sum(numbers_100millon))

numbers_1=list(range(1,20,2))
for number in numbers_1:
	print(number)

numbers_3=list(range(3,31,3))
print(numbers_3)

numbers_3=[]
for number in range(3,31):
	if number%3==0:
		numbers_3.append(number)
print(numbers_3)

numbers_cube=[numbers**3 for numbers in range(1,11)]
for number in numbers_cube:
	print(number)

my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favoriate foods are:")
print(friend_foods)

friend_foods=my_foods
friend_foods.append('ice cream')
print("My friend's favoriate foods are:")
print(friend_foods)
print("My favoriate foods are:")
print(my_foods)

numbers=list(range(1,12))
print(numbers[:3])

length=int(len(numbers)/2)
print(numbers[length-1:length+2])

print(numbers[-3:])

foods=('eggs','meat','chocolate','apple','cola')
for food in foods:
	print(food)
#foods[2]='banana'
foods=('eggs','meat','banana','apple','cola')
print(foods)
