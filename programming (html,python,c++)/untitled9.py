# -*- coding: utf-8 -*-
"""
Created on Fri May 12 08:02:17 2023

@author: USER
"""

def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def multi(x, y):
    return x * y
def divid(x, y):
    return x /y




x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

print("operator:\n")
print("1[addition],2[subtraction],3[multiplication],4[division]")
ans = int(input("Select an operator: "))

while ans >= 5 or ans == 0:
    print("Invalid input, try again! ")
    ans = int(input("Select an operator: "))
else:
    ans <= 4
    if ans == 1:
        print("the sum is: ", add(x, y))
    elif ans == 2:
        print("The difference is: ", sub(x, y))
    elif ans == 3:
        print("The product is: ", multi(x, y))
    elif ans == 4:
        if y == 0:
            print("Cannot be daw ", divid(x, y))
        elif x == 0:
            print("Error", divid(x, y))
        else:
            print("The qoutient is: ", divid(x, y))
    