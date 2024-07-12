# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 08:36:46 2024

@author: Hp
"""
#list comprehension

lst=[]
for num in range (0,20):
    lst.append(num)
print(lst)
    
    
#we can also write the above code in the following manner    
lst=[num for num in range (0,20)]
print(lst)
    
    
####CAPTALIZION ##################
names=['dada','mama','kaka'] 
lst=[name.capitalize() for name in names]
print(lst)


#list comprension with the if statement

#to display the even numbers
def is_even(num):
    return num%2==0

lst=[num for num in range(20) if is_even(num)]
lst

#to display the odd numbers
def is_odd(num):
    return num%2!=0

lst=[num for num in range(20) if is_odd(num)]
lst

#for loop in for loop using list comprensiom
lst=[f"{x}{y}" for x in range(3) for y in range(3)]
lst

#['00', '01', '02', '10', '11', '12', '20', '21', '22']

#dictionary compression
dict={x:x*x for x in range(5)}
dict


#generator
'''it is another way to creating the iterators in a simple
way where it uses the keyword yeild instaed of returning it in a defined
function  '''
gen=(x for x in range(5) )
print(gen)
for num in gen:
    print(num)
    
#if we want to acces one value at a tyme
gen=(x for x in range(5))

next(gen)
next(gen)
next(gen)

#function which returns the multiple value
#this will shoe the even values
def range_even(end):
    for num in range(0,end+1,2):
        yield num
         
for num in range_even(10):
    print(num)


#to access the odd values

def range_odd(end):
    for num in range(1,end+1,2):
        yield num
        
for num in range_odd(10):
    print(num)
    

#i can also access odd values one by one by calling the range_odd function in the generator    
gen=range_odd(10)
next(gen)
next(gen)
next(gen)

#chaining of generator

def lengths(itr):
    for ele in itr:
        yield len(ele)
    
def hide(itr):
    for ele in itr:
        yield ele*'*'
        
'''ele*'*' appears to be the placeholder for the element from the
iterable  this asterisk * isused t replcae a letter as we are 
always see shen we are entering the password at any website
It's a generic representation that doesnt having any specific syntax'
'''
passwords=['not_good','give_me_pass','1010=1010']  


for password in hide(lengths(passwords)):
    print(password)
    
 
#by using user defined 
def lengths(itr):
    for ele in itr:
        yield len(ele)
    
def hide(itr):
    for ele in itr:
        yield ele*'*'
    
passwords=input("Enter Your Password:")

for password in hide(lengths(passwords)):
    print(password,end='')
    
    
    
######################## Afternoon ###############################

#enumerate

lst=["Milk","Egg","Bread"]

for index, item in enumerate(lst,start=1):
    print(f"{index} {item}")
'''
1 Milk
2 Egg
3 Bread'''   

#without enumerator

lst=["Milk","Egg","Bread"]

for index in range(len(lst)):
    print(f"{index+1} {lst[index]}")
'''
1 Milk
2 Egg
3 Bread'''

#use of zip function
#when we wnat to display two or more lists at a time then zip function is used

name=["Mansi","Mummy","Daddy"]
num=[567,678,908]

for nm,inf in zip(name,num):
    print(nm,inf)
'''
Mansi 567
Mummy 678
Daddy 908
'''   
 
name=["Mansi","Mummy","Pappa","Baba"]
num=[567,678,908]

for nm,inf in zip(name,num):
    print(nm,inf)
    
#zip longest function
from itertools import zip_longest
name=["Mansi","Mummy","Daddy","Baba"]
num=[567,678,908]

for nm,inf in zip_longest(name,num):
    print(nm,inf)
    
'''
Mansi 567
Mummy 678
Daddy 908
Baba None'''
#########################################################
#use fill value for excess data as 0 instead of None
from itertools import zip_longest
name=["Mansi","Mummy","Daddy","Baba"]
num=[567,678,908]

for nm,inf in zip_longest(name,num,fillvalue=0):
    print(nm,inf)
    
   
'''
Mansi 567
Mummy 678
Daddy 908
Baba 0'''

#use of all() function 

lst=[2,3,4,6,-3]

if all(lst):
    print("all the values are True")
    #if there are all non zero values it will show the op all values are true
else:
    print("There are null values")
    
 #################################   
lst=[2,3,4,6,-3,0,5]

if all(lst):
    print("all the values are True")
else:
    print("There are null values")
    #if any numm value is consisting then the output willbe there are null value
    
    
#use of any() if there is any non zero value

lst=[0,0,0,0,0]
if any(lst):
    print("There is some non zero value")
else:
    print("There are only zeros")
    
 ####################################################   
    
lst=[0,0,0,-3,0]
if any(lst):
    print("There is some non zero value")
else:
    print("There are only zeros ")
    
#count()

from itertools import count

counter=count()

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

#in this we can also start the count what we need the number 
#like we can also start the counter from 3 or 5

from itertools import count

counter=count(start=4)

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

######################################################

import itertools
#when we want to make a task in repeated manner the this cycle() function is used
instructions=("Eat","Code","Sleep","Repeat")

for instruction in itertools.cycle(instructions):
    print(instruction)
    
    
#repeat()

from itertools import repeat
for msg in repeat("Keep Patience", times=3):
    print(msg)
    
#this will only nshow the output of the "Keep Patience" 3 times only  

#combinations

from itertools import combinations
players=['John','Jani','Janardan'] 
for i in combinations(players,2) :
    print(i)
    
    
'''
('John', 'Jani')
('John', 'Janardan')
('Jani', 'Janardan')'''

#permutations

from itertools import permutations
players=['John','Jani','Janardan'] 
for i in permutations(players,2) :
    print(i)
'''
('John', 'Jani')
('John', 'Janardan')
('Jani', 'John')
('Jani', 'Janardan')
('Janardan', 'John')
('Janardan', 'Jani')'''


#product
from itertools import product
team_a=["rohit","virat","pandya"]
team_b=["ravi","viraj","panda"]

for pair in product(team_a,team_b):
    print (pair)
    
'''('rohit', 'ravi')
('rohit', 'viraj')
('rohit', 'panda')
('virat', 'ravi')
('virat', 'viraj')
('virat', 'panda')
('pandya', 'ravi')
('pandya', 'viraj')
('pandya', 'panda')'''

'''
In python , assignment statements (obj_a,obj_b) do not create real 
copies 
It only creates a new variable with the same referance
So when you want to make actual copies of mutable objects and 
want to modify th copy without affecting the orignl, you have 
to be careful
For real copies you can use the copy module
however for compund/nested objects and custom objects there is 
an important differance between shallow and deep copying

Shallow opies: only one level deep
creates new collection and populates its referacne to neated 
object
deep copies:full independent clone
creates new collection and then recurssively populates it with 
copies of nested  
    
'''

#Assignment operation

#shallow copy and deep copy


list_a=[1,2,3,4]
list_b=list_a

list_a[0]=-10

list_a#[-10, 2, 3, 4]
list_b#[-10, 2, 3, 4]

#both will show the same output because we have modified the variable with the same reference

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




