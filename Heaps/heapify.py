'''
Heapify is the process of fixing a heap so it satisfies the heap property (max or min).

There are two types:

Heapify Down (↓) → used after deletion / building heap
Heapify Up (↑) → used after insertion

🔹 1. Heapify Down (Most Important)

👉 Used when:
You remove the root
You build a heap from an array
📌 Idea
Move a node downwards until the heap property is restored.
Initial (after removing root and placing last element):
        4
       / \
      5   3
     /
    2
Step 1: Compare with children (5, 3)
→ swap with largest (5)
        5
       / \
      4   3
     /
    2
Step 2: Compare 4 with child (2)
→ no swap needed
Final Max Heap ✔️

2. Heapify Up

👉 Used when:
You insert a new element at the end
📌 Idea
Move a node upwards until heap property is satisfied.
Insert 1 into heap:
        2
       / \
      5   3
After insert:
        2
       / \
      5   3
     /
    1
Step 1: Compare with parent (5)
→ swap
        2
       / \
      1   3
     /
    5
Step 2: Compare with parent (2)
→ swap
        1
       / \
      2   3
     /
    5
Final Min Heap ✔️
'''
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        # Start heapifying up from the last index
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, i):
        parent_ind = (i - 1) // 2
        # Your logic: if child is greater than parent, swap and recurse
        if i > 0 and self.heap[i] > self.heap[parent_ind]:
            self.heap[i], self.heap[parent_ind] = self.heap[parent_ind], self.heap[i]
            self._heapify_up(parent_ind)

    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        # Move the last element to the root and sink it down
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_down(self, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        n = len(self.heap)

        # Check if left child exists and is greater than current largest
        if left < n and self.heap[left] > self.heap[largest]:
            largest = left

        # Check if right child exists and is greater than current largest
        if right < n and self.heap[right] > self.heap[largest]:
            largest = right

        # If the largest is one of the children, swap and continue sinking
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._heapify_down(largest)

# --- Quick Test ---
max_heap = MaxHeap()
values = [15, 30, 8, 10, 40]

for v in values:
    max_heap.insert(v)

print("Heap array:", max_heap.heap) 
# Expected: [40, 30, 15, 8, 10] (or similar valid max heap structure)

print("Extracted Max:", max_heap.extract_max()) # 40
print("Heap after extraction:", max_heap.heap)


class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, i):
        parent_ind = (i - 1) // 2
        # Flip: If child is SMALLER than parent, swap
        if i > 0 and self.heap[i] < self.heap[parent_ind]:
            self.heap[i], self.heap[parent_ind] = self.heap[parent_ind], self.heap[i]
            self._heapify_up(parent_ind)

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_down(self, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        n = len(self.heap)

        # Flip: Check if left child is SMALLER than current smallest
        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left

        # Flip: Check if right child is SMALLER than current smallest
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._heapify_down(smallest)

# --- Test ---
min_heap = MinHeap()
for v in [40, 10, 30, 8, 15]:
    min_heap.insert(v)

print("Min Heap array:", min_heap.heap) # The smallest (8) will be at index 0
print("Extracted Min:", min_heap.extract_min()) # 8
