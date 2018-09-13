#!/usr/bin/python3
while 1:
    print("Input exit/Exit to exit.\n")
    username=input("Please input the username:")
    if username.lower() == 'exit':
        break
    content="Hello "+username+"\n"
    print(content)
    with open('guest_book.txt','a') as file_object:
        file_object.write(content)

