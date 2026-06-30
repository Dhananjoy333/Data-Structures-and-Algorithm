'''
DFS (Depth-First-Search) : Depth-first search (DFS) is an algorithm for traversing or searching tree or graph data structures, prioritizing exploring as deep as possible down a branch before backtracking.
Different types of traversal in DFS:
- Inorder traversal
- Preorder traversal
- Postorder traversal

DFS is done through recursion
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
#-------------------------PREORDER TRAVERSAL [Root-Left-Right]-------------------------
# Time complexity : O(N)
# Space complexity : max-height (as recursion involved)
def preorder_traversal(node):
    if node == None:
        return
    print(node.val, end='->')
    preorder_traversal(node.left)
    preorder_traversal(node.right)
preorder_traversal(five)
print()
#-------------------------INORDER TRAVERSAL [Left-Root-Right]-------------------------
# Time complexity : O(N)
# Space complexity : max-height (as recursion involved)
def inorder_traversal(node):
    if node == None:
        return
    inorder_traversal(node.left)
    print(node.val,end="->")
    inorder_traversal(node.right)
inorder_traversal(five)
print()
#-------------------------POSTORDER TRAVERSAL [Left-Right-Root]-------------------------
# Time complexity : O(N)
# Space complexity : max-height (as recursion involved)
def postorder_traversal(node):
    if node == None:
        return
    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node.val,end="->")
postorder_traversal(five)
print()

