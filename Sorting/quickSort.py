def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    while i < j:
        while (arr[i] <= pivot) and (i <= high-1):
            i += 1
        while (arr[j] > pivot) and (j >= low+1):
            j -= 1
        if i<j:
            arr[i],arr[j] = arr[j],arr[i]
    arr[low],arr[j] = arr[j],arr[low]
    return j

def quickSort(arr,low,high):
    if low < high:
        p_inx = partition(arr,low,high)
        quickSort(arr,low,p_inx - 1)
        quickSort(arr,low + 1,high)
#Time Complexity : O(Nlog(N))(Best and avg)
#if all values in arr is same Rime Complexity : O(N^2)(worst case)
#Space Complexity : O(1)