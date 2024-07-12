# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 15:41:45 2024

@author: Hp
"""

#What is the output of this code?
def foo(a, b=4, c=6):
	print(a, b, c)
	 
foo(20, c=12)
#20 4 12

#Write   code  which will give you "Apples"?

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
    
fruits[2]    


#what will be the output

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
fruits[-1] = "Melons"
fruits.append("Lemons")
print(fruits)

#['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Melons', 'Lemons']



#Write a line of code will change the starting_dictionary to the final_dictionary?
starting_dictionary = {
    "a": 9,
	"b": 8,
}
final_dictionary = {
   "a": 9,
   "b": 8,
   "c": 7,
}

starting_dictionary["c"]=7
starting_dictionary

#{'a': 9, 'b': 8, 'c': 7}
