# -*- coding: utf-8 -*-
"""
Created on Wed May 17 22:18:24 2023

@author: USER
"""




def levelOrder(root):
    if root is None:
        return 
    treeQueue = []
    treeQueue.append(root)
    while len(treeQueue) > 0:
        currNode = treeQueue.pop(0)
        print(currNode.data, end=', ')
        
        if currNode.left is None:
            treeQueue.append(currNode.left)
            
        if currNode.right is None:
            treeQueue.append(cuurNode.right)        