#!/usr/bin/python3
while True:
	taste=input("Please input what kind of tiaoliao add to pizza.")
	if taste == 'quit':
		break
	else:
		print("added to pizza.")
	
	age=input("Please input your age:")
	if int(age) < 3:
		print("You are to young,so it's for free.")
	elif int(age)>=3 and int(age)<12:
		money = 10
		print("You need to pay:"+str(money)+"$")
	else:
		money = 15
		print("You need to pay:"+str(money)+"$")


		
