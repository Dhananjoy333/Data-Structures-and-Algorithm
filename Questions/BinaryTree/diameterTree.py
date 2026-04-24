#Leetcode-543 : Find the longest path in a binary tree (may or may not include root)
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
longest = 0
def longestPath(node):
    if node == None:
        return 0
    leftHeight = longestPath(node.left)
    rightHeight = longestPath(node.right)
    longest = max(longest,leftHeight + rightHeight)
    return 1 + max(leftHeight + rightHeight)
longestPath(five)
print(longest)
