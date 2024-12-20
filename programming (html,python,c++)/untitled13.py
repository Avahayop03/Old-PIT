# -*- coding: utf-8 -*-
"""
Created on Wed May 17 22:27:58 2023

@author: USER
"""

class Node:
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None


def printLevelOrder(root):
    if not root:
        return []
 
    queue = []
    queue.append(root)
 
    while(len(queue) > 0):
        print(queue[0].data, end=' ')
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
 
        if node.right is not None:
            queue.append(node.right)



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

printLevelOrder(root)