#!/usr/bin/python3
def make_pizza(size,*toppings):
    print("\nMaking a "+str(size)+"-inch pizza with the following toppings:")
    for topping in toppings:
        print("-" +topping)
#make_pizza('pepperoni')
#make_pizza('mushrooms','green peppers','extra cheese')
#make_pizza('pepperoni','mushrooms','green peppers','extra cheese')
