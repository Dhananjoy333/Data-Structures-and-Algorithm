# #Q.Leetcode-1: Return the indexes of two elements in array that sum up to given value
# def twoSum(arr,val):                                    #TC=O(n^2)
#     for i in range(0,len(arr)):
#         for j in range(0,len(arr)):
#             if(arr[i] + arr[j]==val) and i != j :
#                 return [i,j]
#     return [-1]
# print(twoSum([5,9,1,2,4,15,6,3],10))
#--------------------Optimal------------------
# def twoSum(arr,target):                                 #TC=O(n)
#     seen = {}
#     for i in range(len(arr)):
#         remaining = target - arr[i]
#         if remaining in seen:
#             return [seen[remaining],i]
#         seen[arr[i]] = i
#     return [-1]
# print(twoSum([5,9,1,2,4,15,6,3],10))


#Q.Leetcode-53: Find max subarray sum
# def maxSubArray(arr):                              #TC = O(N^2)
#     total = 0
#     max = float("-inf")
#     for i in range(len(arr)):
#         total = 0
#         for j in range(i,len(arr)):
#             total = total + arr[j]
#             if(total > max):
#                 max = total
#     return max
# print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
#--------------------------optimal (Kadane's algorithm)-------------------------
# def maxSubArray(arr):                                 #TC=O(N)
#     total = 0
#     max = float('-inf')
#     for i in range(0,len(arr)):
#         total = total + arr[i]
#         if(total > max):
#             max = total
#         if(total < 0):
#             total = 0
#     return max
# print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))