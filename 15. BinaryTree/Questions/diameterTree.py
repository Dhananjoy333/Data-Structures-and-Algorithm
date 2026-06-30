#Leetcode-124 : A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
# The path sum of a path is the sum of the node's values in the path.
# Given the root of a binary tree, return the maximum path sum of any non-empty path.
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
r'''
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
    nonlocal longest
    if node == None:
        return 0
    leftHeight = longestPath(node.left)

    rightHeight = longestPath(node.right)
    longest = max(longest,leftHeight + rightHeight)
    return 1 + max(longest,leftHeight + rightHeight)
longestPath(five)
print(longest)
