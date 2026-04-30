# Leetcode - 100: Find if a binary tree is balanced or not 
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
def balancedTree(node):
    if node == None:
        return 0
    leftHeight = balancedTree(node.left)
    if leftHeight == -1:
        return -1
    rightHeight = balancedTree(node.right)
    if rightHeight == -1:
        return -1
    if abs(leftHeight-rightHeight) > 1:
        return -1
    return 1 + max(leftHeight , rightHeight)
ans = balancedTree(five)
if ans < 0 :
    print(False)
else:
    print(True)