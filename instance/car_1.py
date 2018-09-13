#!/usr/bin/python3
def make_car(maker,model,**others):
    car={}
    car['maker']=maker
    car['model']=model
    for key,value in others.items():
        car[key]=value
    return car
car=make_car('subaru','outback',color='blue',tow_package=True)
print(car)
car=make_car('subaru','outback')
print(car)
