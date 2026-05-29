#LeetCode - 701 : Insert val in BST given no duplicate exist
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# def insertIntoBST(root, val):
#     if root is None:
#         return TreeNode(val)
#     if val < root.val:
#         root.left = insertIntoBST(root.left, val)
#     elif val > root.val:
#         root.right = insertIntoBST(root.right, val)
#     return root

def insertIntoBST(root, val):
    if root is None:
        return TreeNode(val)
    curr = root
    while True:
        if val < curr.val:
            if curr.left is None:
                curr.left = TreeNode(val)
                break
            curr = curr.left
        else:
            if curr.right is None:
                curr.right = TreeNode(val)
                break
            curr = curr.right
    return root