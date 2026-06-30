#Q. Find ceiling(larget number smaller than target) and floor(smallest number greater than target)
# def ceilFloor(arr,target):
#     left = 0
#     right = len(arr) - 1
#     lb = len(arr)
#     ub = len(arr)
#     if (target > arr[right]):
#         return [arr[right],-1]
#     if (target < arr[left]):
#         return [-1,arr[left]]
#     while left <= right :
#         mid = int(left +(right - left)/2)
#         if(arr[mid] >= target):
#             lb = mid
#             right = mid - 1
#         else:
#             left = mid + 1
#     left = 0
#     right = len(arr) -1
#     while left <= right :
#         mid = int(left +(right - left)/2)
#         if(arr[mid] > target):
#             ub = mid
#             right = mid - 1
#         else:
#             left = mid + 1
#     if (arr[lb] == target):
#         return [arr[lb],arr[lb]]
#     else:
#         return [arr[lb-1],arr[ub]]
# print(ceilFloor([3,4,4,4,8,9,9,10,12,12,14,15],9))
#------------------------Optimal-------------------------
# def ceilFloor(arr,target):
#     floor = -1
#     ceil = -1
#     left = 0
#     right = len(arr)-1
#     while left <= right:
#         mid = (left + right)//2
#         if arr[mid] == target:
#             return [arr[mid],arr[mid]]
#         elif arr[mid] > target:
#             ceil = arr[mid]
#             right = mid - 1
#         else:
#             floor = arr[mid]
#             left = mid + 1
#     return [floor,ceil]
# print(ceilFloor([3,4,4,4,8,9,9,10,12,12,14,15],11))

#Q. Find the first and last occurences of target
# def occurences(arr,target):
#     first = -1
#     last = -1
#     for i in range(len(arr)):
#         if arr[i] == target:
#             if first == -1:
#                 first = i
#             last = i
#     return [first,last]
# print(occurences([1,2,3,3,3,3,3,5,6,8,9,9,10],7))
#---------------------Optimal-----------------------
# def occurences(arr,target):
#     left = 0
#     right = len(arr) - 1
#     lb = -1
#     ub = -1
#     while left <= right:
#         mid = (left+right)//2
#         if(arr[mid] >= target):
#             lb = mid
#             right = mid - 1
#         else:
#             left = mid + 1 
#     left = 0
#     right = len(arr) -1
#     while left <= right :
#         mid = int(left +(right - left)/2)
#         if(arr[mid] > target):
#             ub = mid
#             right = mid - 1
#         else:
#             left = mid + 1
#     if (arr[ub-1] != target):
#         return [-1,-1]
#     else:
#         return [lb,ub-1]
# print(occurences([1,2,3,3,3,3,3,5,6,8,9,9,10],2))

#Q.Count the occurences of the number
def countOccurences(arr,target):
    left = 0
    right = len(arr) - 1
    lb = -1
    ub = len(arr)
    while left <= right:
        mid = (left+right)//2
        if(arr[mid] >= target):
            lb = mid
            right = mid - 1
        else:
            left = mid + 1 
    left = 0
    right = len(arr) -1
    while left <= right :
        mid = int(left +(right - left)/2)
        if(arr[mid] > target):
            ub = mid
            right = mid - 1
        else:
            left = mid + 1
    if (arr[ub-1] != target):
        return 0
    else:
        return ub-lb
print(countOccurences([1,2,3,3,3,3,3,5,6,8,9,9,10,12,12,12],12))

    