def lowerBound(arr,target):
    left = 0
    right = len(arr) - 1
    lb = len(arr)
    while left <= right:
        mid = int(left + (right-left)/2)
        if(arr[mid] >= target):
            lb = mid
            right = mid - 1             
        else:
            left = mid + 1
    return lb
print(lowerBound([1,1,1,2,3,3,5,6,7,7,7,9,12,12,13],4))

def upperBound(arr,target):
    left = 0
    right = len(arr)
    ub = len(arr)
    while left <= right:
        mid = int(left + (right-left)/2)
        if(arr[mid] > target):
            ub = mid
            right = mid - 1
        else:
            left = mid + 1
    return ub
print(upperBound([1,1,1,2,3,3,5,6,7,7,7,9,12,12,13],4))