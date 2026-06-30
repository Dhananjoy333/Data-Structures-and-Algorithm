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

def maxPathSum(root):
    maxi = float('-inf')
    def dfs(node):
        nonlocal maxi
        if node is None:
            return 0
        leftSum = dfs(node.left)
        if leftSum < 0:
            leftSum = 0
        rightSum = dfs(node.right)
        if rightSum < 0:
            rightSum = 0
        maxi = max(maxi, leftSum + rightSum+node.val)
        return node.val + max(leftSum, rightSum)
    dfs(root)
    return maxi