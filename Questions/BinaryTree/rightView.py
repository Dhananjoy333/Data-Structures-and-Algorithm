from collections import deque


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
def breadthFirst(root):
    res = []
    queue = deque()
    queue.append(five)
    while queue:
        levelSize = len(queue)
        level = []
        for i in range(levelSize):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(level[levelSize-1])
    return res

def reversePostorder(root):
    def dfs(node,level,ans):
        if node is None:
            return
        if len(ans) == level:
            ans.append(node.val)
        if node.right:
            dfs(node.right,level+1,ans)
        if node.left:
            dfs(node.left,level+1,ans)
    dfs(root,0,[])
    