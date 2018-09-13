#!/usr/bin/python3
import random
class Die():
    def __init__(self,sides=6):
        self.sides=sides

    def roll_die(self):
        x=random.randint(1,self.sides)
        return x

dies=Die()
dies=Die(10)
dies=Die(20)
for i in range(10):
    print(dies.roll_die())
