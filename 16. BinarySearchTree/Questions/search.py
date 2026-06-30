#LeetCode - 700 : Search for a given val in BST

# def search(root, val):
#     if root is None:
#         return None
#     if root.val == val:
#         return root
#     if val < root.val:
#         return search(root.left, val)
#     else:
#         return search(root.right, val)


def search(root, val):
    curr = root
    while curr:
        if curr.val == val:
            return curr
        elif val < curr.val:
            curr = curr.left
        else:
            curr = curr.right
    return None