# -*- coding: utf-8 -*-
"""
Created on Sun May  7 21:47:02 2023

@author: USER
"""

lst = []

for i in range(10):
    b = eval(input("Enter elements: "))
    lst.append(b)
    
print("unsorted: ", lst)
for i in range(len(lst)-1):
    #kuwaon ang last element
    for j in range(len(lst)-1 -i):
        if lst[j] > lst [j + 1]:
            lst[j], lst [j + 1] = lst[j+1], lst[j]
            
print("sorted: ", lst)
