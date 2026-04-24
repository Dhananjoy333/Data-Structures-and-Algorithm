# #Q. Merge two sorted array but the numbers should not repeat
# def mergeArr(arr1,arr2):
#     n = len(arr1)
#     m = len(arr2)
#     i = 0
#     j = 0
#     result = []
#     while i < n and j < m:
#         if (arr1[i] <= arr2[j]):
#             if(len(result) == 0):
#                 result.append(arr1[i])
#                 i += 1
#             elif (arr1[i] != result[len(result)-1]) :
#                 result.append(arr1[i])
#                 i += 1
#             else:
#                 i += 1
#         else:
#             if(len(result)==0):
#                 result.append(arr2[j])
#                 j += 1
#             elif (arr2[j] != result[len(result)-1]):
#                 result.append(arr2[j])
#                 j += 1
#             else:
#                 j += 1
#     if j < m:
#         while j < m:
#             if(arr2[j] != result[len(result)-1]):
#                 result.append(arr2[j])
#             j += 1
#     if i < n:
#         while i < n:
#             if(arr1[i] != result[len(result)-1]):
#                 result.append(arr1[i])
#             i += 1
#     return result
# print(mergeArr([1,1,1,1,1,1,1],[2,2,2,2,2,2,2]))

#Q.Leetcode-268: Find the missing number in an array if number are from 0 to n
# def missingVal(arr):
#     for i in range(0,len(arr)):
#         if i not in arr:
#             return i
# print(missingVal([9,6,4,2,3,5,7,0,1]))
# def missingVal(arr):
#     hashMap = {}
#     for i in range(len(arr)+1):
#         hashMap[i] = 0
#     for i in arr:
#         if i in hashMap:
#             hashMap[i] += 1
#     for i in range(len(arr)):
#         if hashMap[i] == 0:
#             return i
#-----------------------optimal-------------------
# def missingVal(arr):
#     n = len(arr)
#     expected = n * (n + 1) // 2
#     actual = sum(arr)
#     return expected - actual
# print(missingVal([9,6,4,2,3,5,7,0,1]))
# def missingVal(arr):                       #interview favorite
#     xor = 0
#     for i in range(len(arr) + 1):
#         xor ^= i
#     for num in arr:
#         xor ^= num
#     return xor
# print(missingVal([9,6,4,2,3,5,7,0,1]))

#Q.Leetcode-485: Count maximum consecutive 1
# def countFreq(arr):
#     temp= 0
#     count=0
#     for i in arr:
#         if i == 1 :
#             temp += 1
#         if temp > count:
#             count = temp
#         if i != 1:
#             temp = 0
#     return count
# print(countFreq([0,0,0,1,1,0,0,1,1,1,1,1]))