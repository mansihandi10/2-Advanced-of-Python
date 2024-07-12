# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 08:16:01 2024

@author: Mansi Handi
"""
'''1 level deep it is only aoolicable for shallow copy
list_a=[1,2,3,4]'''

import copy
list_a=[1,2,3,4]

list_b=copy.copy(list_a)
list_b[0]=-10

list_a#[1, 2, 3, 4]
list_b#[1, 2, 3, 4]

'''2 level deep shallow copy will not be applicable for 2 level deep
list_a=[[1,2,3,4],[5,6,7,8]]'''

import copy
list_a=[[1,2,3,4],[5,6,7,8]]

list_b=copy.copy(list_a)
list_a[0][0]=-10

list_a#[[-10, 2, 3, 4], [5, 6, 7, 8]]
list_b#[[-10, 2, 3, 4], [5, 6, 7, 8]]

# by above example we can conclude that 2 level deep is not applicable for 
#the 2 level deep beacse it is displaying same items for the lists


'''Deep Copiess
for deep copy use the function for copy.deepcopy()
it is going to create fully independent clones
import copy'''
list_a=[[1,2,3,4],[5,6,7,8]]

list_b=copy.deepcopy(list_a)
list_a[0][0]=-10

list_a#[[-10, 2, 3, 4], [5, 6, 7, 8]]
list_b#[[1, 2, 3, 4], [5, 6, 7, 8]]

#reading data in various formates

#check for working directory
import pandas as pd
f1=pd.read_csv("buzzers.csv")
#there are two types of path called as relative path and absolute path
#in this example i used the relative path=buzzers.csv
#absolute pathb ="E:/1-Python/buzzers.csv"
import os
with open("buzzers.csv") as raw_data:
    print(raw_data.read())
'''"TIME,DESTINATION"
"09:35,FREEPORT"
"17:00,FREEPORT"

"19:00,WEST END"
"10:45,TREASURE CAY"

"11:45,ROCK SOUND"
"17:55,ROCK SOUND"'''

##################### AFTERNOON ######################

#reading csv data as a list


import csv
with open("C:/1-Python/buzzers.csv.") as raw_data:
    print(raw_data.read())

#Reading csv data as dictionar
import csv
with open("C:/1-Python/buzzers.csv") as raw_data:
    for line in csv.DictReader(raw_data):
        print(line)
    
with open("buzzers.csv") as data:
    flights={}
    for line in data:
        k,v=line.split(',')
        flights[k]=v
    flights
    
    
def plus_one(number):
    number1=number+1
    return number1

plus_one(9)

#function in side the function

def plus_one(number):
    
    def add_one(number):
        number1=number+1
        return number1
    result=add_one(number)
    return result

plus_one(9)

#passing functions as a argument

def plus_one(num):
    num1=num + 1   
    return num1


def function_call(function):
    num1=function(7)
    return num1

function_call(plus_one)

#function returning the other function

def hello_function():
    def say_hi():
        return 'Hi'
    return say_hi
hello=hello_function()
hello()

#need of decoraters
#this is very important interview point of view
import time
def cal_sqr(nums):
    start=time.time()
    result=[]
    for num in nums:
        result.append(num*num)
    end=time.time()
    total_t=(end-start)*1000
    print(total_t)
    return result

import time
def cal_cube(nums):
    start=time.time()
    result=[]
    for num in nums:
        result.append(num*num*num)
    end=time.time()
    total_t=(end-start)*1000
    print(total_t)
    return result

array=range(1,10000)
out_sqr=cal_sqr(array)#0.9312629699707031
out_cube=cal_cube(array)#0.9975433349609375
