#!/usr/bin/python3
cat_txt='cats.txt'
dog_txt='dogs.txt'
try:
    with open(cat_txt) as cat_object:
        cat_content=cat_object.read()
    with open(dog_txt) as dog_object:
        dog_content=dog_object.read()
except FileNotFoundError:
#    print('File not exist,please check.')
    pass
else:
    print(cat_content)
    print(dog_content)
