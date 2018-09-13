#!/usr/bin/python3
import json

def input_number():
    number=input("Input the you liked number:")
    number_file='numbers.txt'
    with open(number_file,'w')as f_obj:
        json.dump(number,f_obj)

def output_number():
    number_file='numbers.txt'
    try:
        with open(number_file) as f_obj:
            number=json.load(f_obj)
    except FileNotFoundError:
        input_number()
    else:
        print("I know your favorite numbers!It's "+number)

#input_number()
output_number()
