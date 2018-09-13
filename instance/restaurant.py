#!/usr/bin/python3
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_serverd=0

    def describe_restaurant(self):
        print("restaurant name is:"+self.restaurant_name)
        print("restaurant cuisine is:"+self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is opening.")

    def set_number_served(self,server_number):
        self.number_serverd=server_number
        print("The restaurant has serverd numbers:"+str(self.number_serverd))

    def increment_number_served(self,number):
        self.number_serverd+=number
        print("The restaurant today serverd numbers:"+str(self.number_serverd))

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=[]

    def show_flavor(self,favoriates):
        self.flavors=favoriates
        print(self.flavors)

my_restaurant=Restaurant("China's restaurant","sweet")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
print(my_restaurant.number_serverd)
my_restaurant.number_serverd=10
print(my_restaurant.number_serverd)
my_restaurant.set_number_served(100)
my_restaurant.increment_number_served(200)
ice_restaurant=IceCreamStand("China's restaurant","sweet")
favo=['a','b','c']
ice_restaurant.show_flavor(favo)
