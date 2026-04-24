#Selection sort is a simple sorting algorithm that works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and swapping it with the first unsorted element. The algorithm maintains two subarrays: one that is already sorted and one that is unsorted. Initially, the sorted subarray is empty and the unsorted subarray contains all the elements. The algorithm iteratively selects the minimum element from the unsorted subarray and moves it to the end of the sorted subarray until all elements are sorted.

#Time complexity is O(N^2)

def selection_sort(arr):
    for i in range(0, len(arr)):
        minInd = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minInd]:
                minInd = j
        arr[i], arr[minInd] = arr[minInd], arr[i]
    return arr
arr=[6,7,9,5,4,12,45,6,1,2,3]
print(selection_sort(arr))