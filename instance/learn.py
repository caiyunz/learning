#!/usr/bin/python3
with open('learning_python.txt') as file_object:
#    contents=file_object.read()
#    print(contents)
#    for line in file_object:
#        print(line.rstrip())
    lines=file_object.readlines()
for line in lines:
    print(line.strip())
