#Inside stack and queues mandatory topics
# 1. Implement stack using Array
# 2. Implement Queue using Array
# 3. Implement stack using Queue
# 4. Implement Queue using stack
# 5. Implement stack using LinkedList
# 6. Implement Queue using LinkedList
# 7. Check for balanced parenthesis
# 8. Implement min stack

#---------------Implement stack using Array---------------
class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):                # O(1)
        return len(self.items) == 0
    
    def push(self,item):               # O(1)
        self.items.append(item)

    def pop(self):                     # O(1)
        if len(self.items) == 0:
            return "Cannot pop, stack is empty"
        x = self.items.pop()
        return x
    
    def top(self):                     # O(1)
        if len(self.items) == 0:
            return "Cannot top, stack is empty"
        return self.items[-1]
    
    def size(self):                   # O(1)
        return len(self.items)
    
    def see(self):
        print(self.items)
    
stack = Stack()
stack.push(5)
stack.push(4)
stack.push(9)
stack.push(11)
stack.push(14)
stack.see()

#------------------Implement Queue using Array-------------------
class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):               #O(1)
        return len(self.items) == 0
    
    def enqueue(self,val):            #O(1)
        return self.items.append(val)
    
    def dequeue(self):                #O(N)
        if len(self.items) == 0:
            return "Cannot dequeue, Queue is empty"
        x = self.items.pop(0)
        return x
    
    def front(self):                  #O(1)
        if len(self.items) == 0:
            return "Cannot peek, Queue is empty"
        return self.items[0]
    
    def rear(self):                    #O(1)
        if len(self.items) == 0:
            return "Cannot peek, Queue is empty"
        return self.items[-1]
    
    def size(self):                    #O(1)
        return len(self.items)
    
    def see(self):                     #O(1)
        print(self.items)

queue = Queue()
queue.enqueue(6)
queue.enqueue(9)
queue.enqueue(12)
queue.enqueue(11)
queue.enqueue(5)
queue.see()
queue.dequeue()
queue.see()

#--------------------------Implement stack using Queue------------------
#push(x) --> insert to the end, rotate the elements of queue by len(queue)-1 this bring last inserted to first so when we pop() as required in queue(FIFO) element in first position comes out but the actual element that came out was the most recently added element i.e, (LIFO)
from collections import deque
class StackUsingQueue:
    def __init__(self):
        self.queue = deque()
    
    def is_empty(self):                # O(1)
        return len(self.queue) == 0
    
    def push(self,item):               # O(1)
        self.queue.append(item)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self):                     # O(1)
        if len(self.queue) == 0:
            return "Cannot pop, stack is empty"
        return self.queue.popleft()
    
    def peek(self):                     # O(1)
        if len(self.queue) == 0:
            return "Cannot top, stack is empty"
        return self.queue[0]
    
    def size(self):                   # O(1)
        return len(self.queue)
    
    def see(self):
        print(self.queue)

#----------------------Implement Queue using stack-----------------
#push()--> 1. transfer all element from stack1 --> stack2
#          2. insert element to stack1 
#          3. transfer stack2 --> stack1
class QueueUsingStack:
    def __init__(self):
        self.st1 = []
        self.st2 = []

    def push(self,val):
        while self.st1:
            self.st2.append(self.st1.pop())
        self.st1.append(val)
        while self.st2:
            self.st1.append(self.st2.pop())

    def pop(self):
        if not self.st1:
            print("Stack is empty")
            return -1
        top_element = self.st1.pop()
        return top_element
    
    def peek(self):
        if not self.st1:
            print("Stack is empty")
            return -1
        return self.st1[-1]
    
    def is_empty(self):                # O(1)
        return not self.st1
    
#--------------------Implement stack using DoublyLinkedList----------------
class Node:
    def __init__(self,val):
        self.next = None
        self.val = val
        self.prev = None

class StackWithDll:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def push(self,val):
        newNode = Node(val)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
    
    def pop(self):
        if self.head is None:
            print("No items in stack")
            return     
        value = self.tail.val
        if self.head == self.tail:   # only one node
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return value
    
    def peek(self):
        if self.head is None:
            print("No items in stack")
            return
        return self.tail.val
    
    def see(self):
        current = self.head
        if self.head is None:
            print("No items in stack")
            return
        while current is not None:
            print(current.val,end=" ")
            current = current.next
        print()

    def is_empty(self):
        return self.head is None

    
#--------------------Implement Queue using DoublyLinkedList----------------
class Node:
    def __init__(self,val):
        self.next = None
        self.val = val
        self.prev = None

class QueueWithDll:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self,val):
        newNode = Node(val)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
    
    def dequeue(self):
        if self.head is None:
            print("Queue is empty")
            return     
        value = self.head.val
        if self.head == self.tail:   # only one node
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return value
    
    def rear(self):
        if self.head is None:
            print("Queue is empty")
            return
        return self.tail.val
    
    def front(self):
        if self.head is None:
            print("Queue is empty")
            return
        return self.head.val
    
    def see(self):
        current = self.head
        if self.head is None:
            print("Queue is empty")
            return
        while current is not None:
            print(current.val,end=" ")
            current = current.next
        print()

    def is_empty(self):
        return self.head is None

        
