#!/usr/bin/python3
with open('the.txt') as the_object:
    contents=the_object.read()
#lists=contents.split()
print(contents.lower().count('the'))

