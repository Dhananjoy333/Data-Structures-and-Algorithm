# What is Binary Tree?
# A binary tree is a hierarchical, non-linear data structure where each node has at most two children, referred to as the left child and the right child
# Root : The starting node for the entire tree is called root.
# Node : Each and every container that makes the tree is called node.
# Subtree : A sub-part of the entire tree which can make its own tree. End nodes can also be considered subtree, and have their own root.
# Children : If we take any node the nodes which comes out of it are its children.
# Parent : Node from which the selected node came from .
# Ancestors : All nodes which are direct parents of selected node.
# LeafNode: Nodes which have no children.

#---------------------------TYPES OF BINARY TREE------------------------------
#1.Full Binary Tree: All nodes must have 2 or 0 children.
#2.Complete Binary Tree: All levels must be full except the last level && if last level is not full all nodes must be in extreme left side.
#3.Perfect Binary Tree: All leaf node must be at same level && All non-leaf node must have 2 children.
#4.Balanced Binary Tree: height difference between left and right subtree at any node must be at max 1.
#5.Degenerate Binary Tree: Every node has only 1 child.

#--------------------------IMPLEMENTATION BINARY TREE---------------------------
class Node:
    def __init__(self,val):
        self.left = None
        self.val = val
        self.right = None

'''
                    drinks
                    /    \
                hot      cold
               /   \     /   \
            tea  coffee cola  fanta
'''
drinks = Node('drinks')
hot = Node('hot')
cold = Node('cold')
tea = Node('tea')
coffee = Node('coffee')
cola = Node('cola')
fanta = Node('fanta')

drinks.left = hot
drinks.right = cold

hot.left = tea
hot.right = coffee

cold.left = fanta
cold.right = cola

print(drinks.left.left.val)

      