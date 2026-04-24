'''
BFS (Breadth First Search) : Breadth-First Search (BFS) is a foundational algorithm used to traverse or search tree or graph data structures. It starts at a designated node and explores all neighboring nodes at the current level before moving on to the nodes at the next depth level.
- Levelorder traversal
we use Queue for this and run on for loop
'''
class Node:
    def __init__(self,val):
        self.left = None
        self.val = val
        self.right = None

'''
                                5
                            /       \
                           3         4
                        /     \     /   \
                        2      9   8     10
                                  / \    
                                  1  6
'''
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
eight = Node(8)
nine = Node(9)
ten = Node(10)

five.left = three
five.right = four
three.left = two
three.right = nine
four.left = eight
four.right = ten
eight.left = one
eight.right = six
#----------------------LEVELORDER TRAVERSAL-------------------------
# Time complexity = O(N)
# Space complexity = O(N) 
from collections import deque
def level_order_traversal(node):
    res = []
    queue = deque([])
    queue.append(node)
    while len(queue) != 0:
        e = queue.popleft()
        res.append(e.val)
        if e.left is not None:
            queue.append(e.left)
        if e.right is not None:
            queue.append(e.right)
    return res
print(level_order_traversal(five))
