# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 08:29:37 2024

@author: Hp
"""

'''sometimes a single peice of code might be suspected to 
have more than one type of error for handling such type of 
situations we can have multiple expect blocks for a single
try block'''
try:
    numerator=50
    denom=int(input("Enter the input: "))
    print(numerator/denom)
    print("Division is performed Successfully")
except ZeroDivisionError:
    print("Denominator sould be greater than 0")
except ValueError:
    print("Only integers should be entered")

'''
Enter the input: 50
1.0
Division is performed Successfully

Enter the input0
Denominator sould be greater than 0

Enter the inputww
Only integers should be entered
'''

#Handling the erros without naming them
#any other exceptions also can be handled using this methos

try:
    numerator=50
    denom=int(input("Enter the input"))
    print(numerator/denom)
    print("Division is performed Successfully")
except ValueError:
    print("Only integers should be entered")
    
except :
    print("Oops...., some exeption is raised")
    
#handlingb exceptions using try,expect and else

try:
    numerator=50
    denom=int(input("Enter the input"))
    result=numerator/denom
    print("Division is performed Successfully")
except ValueError:
    print("Only integers should be entered")
    
except :
    print("Oops...., some exeption is raised")

else:
    print("The result of the division is", result)
    
#handling exceptions using try,expect, and finally

try:
    numerator=50
    denom=int(input("Enter the input"))
    result=numerator/denom
    print("Division is performed Successfully")
except ValueError:
    print("Only integers should be entered")
    
except :
    print("Oops...., some exeption is raised")

else:
    print("The result of the division is", result)
finally:
    print("Over and Out")
    
 
    
    

        
    