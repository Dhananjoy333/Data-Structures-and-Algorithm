def merge_array(left,right):
    i,j = 0,0
    n,m = len(left),len(right)
    result = []
    while i < n and j < m:
        if (left[i] <= right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < n:
        while i < n:
            result.append(left[i])
            i += 1
    if j < m:
        while j < m:
            result.append(right[j])
            j += 1
    return result

def mergeSort(arr):
    if (len(arr) <= 1):
        return arr
    mid = len(arr)//2
    left_arr = arr[ :mid]
    right_arr = arr[mid: ]
    left = mergeSort(left_arr)
    right = mergeSort(right_arr)
    return merge_array(left,right)
arr=[6,7,9,5,4,12,45,6,1,2,3]
sorted = mergeSort(arr)
print(sorted)

#Time Complexity : O(Nlog(N))
#space complexity : O(N)