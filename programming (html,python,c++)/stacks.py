from queue import LifoQueue

stack = LifoQueue(maxsize=10) #maximum of 10 elements

print("Enter 10 elements\n")
for i in range(10):
    element = input(f"Enter element {i + 1}: ")
    stack.put(element)
   
print("\nFull:", stack.full(),", Can't add another element.")



print("\nFirst element: ", stack.queue[-1])
print("Last element: ", stack.queue[0])

print("\nLIFO order:") #last in first out order
while not stack.empty():
    item = stack.get() 
    print(item, end=' ')