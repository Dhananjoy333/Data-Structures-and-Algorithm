class MinHeap:
    def __init__(self):
        self.heap = []
    
    def insert(self,val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)
    
    def _heapify_up(self,i):
        parent = (i-1)//2
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i],self.heap[parent] = self.heap[parent],self.heap[i]
            self._heapify_up(parent)
    
    def getMin(self):
        return self.heap[0]
    
    def extractMin(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root
    
    def _heapify_down(self,i):
        smallest = i
        leftChild = 2 * i + 1
        rightChild = 2 * i + 2
        n = len(self.heap)
        
        if leftChild < n and self.heap[leftChild] < self.heap[smallest]:
            smallest = leftChild
        
        if rightChild < n and self.heap[rightChild] < self.heap[smallest]:
            smallest = rightChild
        
        if smallest != i:
            self.heap[i],self.heap[smallest] = self.heap[smallest],self.heap[i]
            self._heapify_down(smallest)
    
    def size(self):
        return len(self.heap)
    
    def isEmpty(self):
        if len(self.heap) == 0:
            return True
        else:
            return False
    
    def changeKey(self,i,new_val):
        if self.heap[i] > new_val:
            self.heap[i] = new_val
            self._heapify_up(i)
        else:
            self.heap[i] = new_val
            self._heapify_down(i)

arr = [5,8,3,8,12,66,32,12,45]
minHeap = MinHeap()
for v in arr:
    minHeap.insert(v)
print("Min Heap array:", minHeap.heap)
minHeap.changeKey(len(minHeap.heap) - 1,1)
print("After changing key:", minHeap.heap)
print(minHeap.extractMin())
print("After extracting min:", minHeap.heap)       