arr=[6,7,9,5,4,12,45,6,1,2,3]
def insertionSort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
insertionSort(arr)
print(arr)

#Time complexity is O(N^2)