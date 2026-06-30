#A stack is a data structure that follows the Last In First Out (LIFO) principle. It can be implemented using a list or a deque in Python.
#Here is an example of how to implement a stack using a deque:

#with list this is ineffective because of the time complexity of pop and append operations
stack = []
stack.append("apple")
stack.append("mango")
stack.append("orange")
print(stack)
print(stack.pop())


#more efficient implementation using deque
from collections import deque
stack = deque()
stack.append("apple")
stack.append("mango")
stack.append("orange")

print(stack)
print(stack.pop())
print(stack)