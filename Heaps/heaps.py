'''
A heap is a special type of binary tree used mainly to efficiently get the minimum or maximum element.

🔹 What is a Heap?
A heap is a complete binary tree that follows a specific rule:

1. Max Heap
Parent node is greater than or equal to its children
The largest element is always at the root
        10
       /  \
      5    3
     / \
    2   4

2. Min Heap
Parent node is less than or equal to its children
The smallest element is always at the root
        2
       / \
      5   3
     / \
    10  4

🔹 Key Properties
Complete Binary Tree
All levels filled except possibly last
Last level filled left → right
Heap Property
Max heap → parent ≥ children
Min heap → parent ≤ children

Array Representation
Heaps are usually stored in arrays (no pointers needed):
For index i:
Left child → 2i + 1
Right child → 2i + 2
Parent → (i - 1) // 2

Example:
Heap:       10
          /    \
         5      3
        / \
       2   4

Array: [10, 5, 3, 2, 4]

Internal Nodes in a Heap 
Internal nodes are the nodes that have at least one child.
In simple terms: not leaf nodes
        10
       /  \
      5    3
     / \
    2   4
Internal Nodes
10 (has children 5, 3)
5 (has children 2, 4)
3 ❌ (no children → leaf)
2 ❌ (leaf)
4 ❌ (leaf)

👉 So, internal nodes = [10, 5]

For Complete Binary Tree
number of internal nodes = n - 1 (n = number of nodes) 

For Almost complete Binary Tree
        10
       /  \
      5    3
     / \
    2   4
Heap: [10, 5, 3, 2, 4]
Index:  0   1  2  3  4
index of leaf nodes : 2,3,4 or n//2 -> n-1
index of leaf nodes : 0 -> (n//2)-1
'''