# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 08:55:24 2024

@author: Hp
"""
'''A python decorater is a function that takes in a function and returns 
it by adding son=me another functionality'''
def say_hi():
    return "hello, mansi is here"
def uppercase_decoder(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper

decorate=uppercase_decoder(say_hi)
decorate()       
 
#we can also write this program with the help of another by only calling the function using '@'   
def uppercase_decoder(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@uppercase_decoder
def say_hi():
    return "hello, mansi is here"

# Call the decorated function
print(say_hi())

def split_string(function):#code to split string
    def wrapper():
        func = function()
        splitted_string=func.split()
        return splitted_string
    return wrapper

def uppercase_decorator(function): #code to make uppercase
    def wrapper(): 
        func = function()
        make_uppercase= func.upper()
        return make_uppercase
    return wrapper

    
@split_string #decorator  called  
@uppercase_decorator  
def say_hi():
    return 'hello boss'
say_hi()

####################### Afternoon ###########################