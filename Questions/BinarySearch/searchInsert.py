#Q.Leetcode-35: Search Insert position (if target exist return target position else return the position where target can go)
# def searchInsetPos(arr,target):
#     left = 0
#     right = len(arr) - 1
#     lb = len(arr)
#     while left <= right:
#         mid = int(left + (right-left)/2)
#         if(arr[mid] >= target):
#             lb = mid
#             right = mid - 1
#         else:
#             left = mid + 1
#     return lb 
# print(searchInsetPos([1,3,4,5,8,9,14,15,15,15,15,19,20,21],17)) 
