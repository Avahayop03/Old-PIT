# -*- coding: utf-8 -*-
"""
Created on Sun May  7 21:34:36 2023

@author: USER
"""

#bubble sort

lst = []

for i in range(10):
    a = eval(input("enter elements: "))
    lst.append(a)

print("unsorted: ")    
for i in range(len(lst)-1):
    
    for j in range(len(lst)-1 -i):
        if lst[j] > lst [j+1]:
            lst[j+1], lst[j] = lst [j], lst[j+1]
            
print("bubble sort: ", lst)
    