#!/usr/bin/python3
def show_magicians(magician_names):
    for magician in magician_names:
        print("Hello "+magician)
def make_great(magician_names):
    for num in range(len(magician_names)):
        magician_names[num]="the Great "+magician_names[num]
    return magician_names
magician_name=["Eric","Bob","Toms"]
show_magicians(magician_name)
magician_names=make_great(magician_name[:])
show_magicians(magician_name)
show_magicians(magician_names)
