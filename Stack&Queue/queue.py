#A queue is a data structure that follows the First In First Out (FIFO) principle. It can be implemented using a list or a deque in Python.
#enqueue operation is used to add an element to the rear of the queue, while dequeue operation is used to remove an element from the front of the queue.

# A simple implementation of a queue using a list in Python it is not efficient because of the time complexity of pop(0) operation
q=[]
q.append(1)
q.append(2)
q.append(3)
print(q)
print(q.pop(0))

# A more efficient implementation of a queue using a deque in Python
from collections import deque
q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)
print(q.popleft())

#Using queue.Queue is a thread-safe implementation of a queue in Python. It is useful for multi-threaded programming.
from queue import Queue
q = Queue(maxsize=3)
q.put(1)
q.put(2)
q.put(3)
print(q.get())
