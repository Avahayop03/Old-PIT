# -*- coding: utf-8 -*-
"""
Created on Sun May  7 22:47:48 2023

@author: USER
"""

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 
    else:
        return (x * factorial(x-1))


num = 3
print("The factorial of", num, "is", factorial(num))