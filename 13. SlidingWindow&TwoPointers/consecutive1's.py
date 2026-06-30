#Q.Leetcode-1004: find max consecutive 1's also will we given a number upto which we can change the numbers into 1 [111000111100]
#------------------------brute---------------------
# def consecutiveOnes(arr,num):
#     maxi = 0
#     n = len(arr)
#     for i in range(0,n):
#         zeros = 0
#         for j in range(i,n):
#             if arr[j] == 0:
#                 zeros += 1
#             if zeros > num:
#                 break
#             maxi = max(maxi, j-i+1)
#     return maxi
#--------------------------better----------------------
# def consecutiveOnes(arr,num):
#     n = len(arr)
#     left  = 0
#     right = 0
#     maxi = 0
#     zeros = 0
#     while right < n:
#         if arr[right] == 0:
#             zeros += 1
#         while zeros > num :
#             if arr[left] == 0:
#                 zeros -= 1
#             left += 1
#         if zeros <= num:
#             maxi = max(maxi, right - left +1)
#         right += 1
#     return maxi
# #-------------------optimal----------------------
# def consecutiveOnes(arr,num):
#     n = len(arr)
#     left  = 0
#     right = 0
#     maxi = 0
#     zeros = 0
#     while right < n:
#         if arr[right] == 0:
#             zeros += 1
#         if zeros > num :
#             if arr[left] == 0:
#                 zeros -= 1
#             left += 1
#         if zeros <= num:
#             maxi = max(maxi, right - left +1)
#         right += 1
#     return maxi
