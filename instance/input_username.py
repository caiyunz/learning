#!/usr/bin/python3
username=input("Please input the user name:")
if username:
    with open('guest.txt','a') as file_object:
        file_object.write(username+'\n')

