#!/usr/bin/python3
names=['bob','eric','tom','groot']
for name in names:
# 	print(name.title())
	print("Hello,"+name.title()+"\nWelcome to Python world!")
	
motorcycles=['honda','yamaha','suzuki']
del motorcycles[0]
print("del list:")
print(motorcycles)

motorcycles.append('honda')#append var into list behind
motorcycles.insert(0,'honda')#insert var into any location
popped_motorcycle=motorcycles.pop()
print ("pop var: "+popped_motorcycle)
print("pop list:")
print(motorcycles)


motorcycles.remove('yamaha')
print("remove list: ")
print(motorcycles)

motorcycles=['honda','yamaha','suzuki']
remove_var='honda'

motorcycles.remove(remove_var)
print("remove var"+remove_var)
print("remove list: ")
print(motorcycles)

visitors=['zhaocy','groot','xiaobao']
print(visitors)

position=visitors.index('xiaobao')
print("Position:"+str(position))

people_not="xiaobao"
#visitors.remove(people_not)
#print(visitors)
#print(people_not)

#visitors.append("caiyunz")
print(visitors)
visitors[position]="caiyunz"
for visitor in visitors:
	print("Welcome to family party:"+visitor)
	
print("We have a big dining table,we will invite more people!")
visitors.insert(0,'Bob')
print(visitors)
length=len(visitors)
position=int(length/2)
visitors.insert(position,'Eric')
print(visitors) 
visitors.append('Tom')
print(visitors)
for pos in range(len(visitors)):
	print("Welcome to family party:"+visitors[pos])
print("I'm so sorry,my dining table can't arrive in time,so we can only invite two customer!")
print(len(visitors))
for i in range(len(visitors)):
	print(i)
	if len(visitors) != 2:
		visitors.pop()
		#print(len(visitors))
		#print(visitors)
print(visitors)
