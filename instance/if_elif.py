#!/usr/bin/python3
alien_color=['green','yellow','red']
#alien=input("Please input the alien color.")
alien="green"
if alien == 'green':
	print("Congratulations!You have owned 5 point.")
else:
	print("You have owned 10 point.")

requested_toppings=['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry,we are out of green peppers right now.")
	else:
		print("Adding " + requested_topping + ".")
print("Finished making your pizza!\n") 

#to make sure list is not null
#requested_toppings=['mushrooms','green peppers']
requested_toppings=[]
if requested_toppings:
	for requested_topping in requested_toppings:
		print("Adding "+requested_topping + ".")
else:
	print("Are you sure you want a plain pizza?\n")

available_toppings=['mushrooms','olives','green peppers','pepperoni',
'pineapple','extra cheese']
requested_toppings=['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding "+requested_topping +".")
	else:
		print("Sorry,we don't have "+requested_topping+".")
print("Finished making your pizza!\n")

#users=['bob','eric','tom','admin','groot']
users=[]
if users:
	for user in users:
		if user == 'admin':
			print("Hello admin,would you like to see a status report?")
		else:
			print("Hello Eric,thank you for logging in again.")
else:
	print("We need to find users!\n")
	
current_users=['bob','eric','tom','admin','groot']
new_users=['Groot','TOM','yangzi','xiaobao','qiqi']
for user in new_users:
	if user.lower() in current_users:
		print("Please use another user name "+user+",because this name has used in another place.thanks!")
	else:
		print("Hello,"+user.title()+" welcome to www world")

numbers=list(range(1,10))
for number in numbers:
	#print(number)
	if(number==1):
		print("1st")
	elif(number==2):
		print("2nd")
	elif(number==3):
		print("3rd")
	else:
		print(str(number)+"th")
