#!/usr/bin/python3
class Employee():
    def __init__(self,first,last,salary):
        self.first=first
        self.last=last
        self.salary=salary
    
    def give_raise(self,add=5000):
        self.salary+=add
        print(self.salary)
        return self.salary
