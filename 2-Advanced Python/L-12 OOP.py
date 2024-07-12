# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 08:18:50 2024

@author: Hp

object oriented programming
"""

class Human:
    def __init__(self,n,o):
        self.name=n
        self.occupation=o
        
    def do_work(self):
        if self.occupation=="Tennis Player":
            print(self.name,"Play Tennis")
        elif self.occupation=="Actor":
            print(self.name,"Shoots Film")
            
    def speaks(self):
        print(self.name,"Says How are you?")
x=Human("XYZ","Actor")
x.do_work()
x.speaks()

a=Human("abc","Tennis Player")
a.do_work()
a.speaks()

#Single inheritance in python
class vehicle:
    def general_usage(self):
        print("General use: Transportation")
        
class Car(vehicle):
    def _init_(self):
        print("I'm Car")
        self.wheels=4
        self.has_roof=True
        

    def specific_usage(self):
        self.general_usage()
        print("Specific use:Commute to work,Vacation with family")        


class MotorCycle(vehicle):
    def _init_(self):
        print("I'm Motor-cycle")
        self.wheels=2
        self.has_roof=False
        

    def specific_usage(self):
        self.general_usage()
        print("Specific use:Local communication, racing")


c=Car()
c.specific_usage()
m=MotorCycle()
m.specific_usage()

#multiple inheritance in Python

class Father:
    def skills(self):
        print("I like Gardening and Sports")

class Mother:
    def skills(self):
        print("I like Cooking and Art")
        
        
class Child():
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("I like Sports")
        
c=Child()
c.skills()

'''I like Gardening and Sports
I like Cooking and Art
I like Sports'''
