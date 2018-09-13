#!/usr/bin/python3
def describe_pet(pet_name,animal_type='dog'):
    """show pet's animal"""
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet('harry','hamster')
describe_pet('willie')
describe_pet(animal_type="hamster",pet_name="harry")
describe_pet(pet_name="willie",animal_type="dog")
