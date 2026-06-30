#Leetcode-104 : Find the max depth of BT
class Node:
    def __init__(self,val):
        self.left = None
        self.val = val
        self.right = None

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)
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
one.left = seven
'''
                                5
                            /       \
                           3         4
                        /     \     /   \
                        2      9   8     10
                                  / \    
                                  1  6
                                 /
                                 7
'''

#-------------------------with recursion(better)--------------------
def treeHeight(node):
    if node == None:
        return 0
    leftHeight = treeHeight(node.left)
    rightHeight = treeHeight(node.right)
    return 1 + max(leftHeight,rightHeight)
print(treeHeight(five))

#--------------------------with iteration---------------------
from collections import deque
def level_order_traversal(node):
    height = 0
    queue = deque([])
    queue.append(node)
    while len(queue) != 0:
        level_size = len(queue)
        height += 1
        for _ in range(level_size):
            e = queue.popleft()
            if e.left is not None:
                queue.append(e.left)
            if e.right is not None:
                queue.append(e.right)
    return height   
print(level_order_traversal(five))
