def nextGreater(arr):
    res = [-1] * len(arr)
    if len(arr) == 0 or len(arr) == 1:
        return res
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j] > arr[i]:
                res[i] = arr[j]
                break
        if j==len(arr):
            res[i] = -1
    return res