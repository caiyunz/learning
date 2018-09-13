#!/usr/bin/python3
filename='pi_digits.txt'
with open(filename) as file_object:
#    contents = file_object.read()
#    print(contents)
#    for line in file_object:
#        print(line.rstrip())
    lines=file_object.readlines()
for line in lines:
    print(line.rstrip())
