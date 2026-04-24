#Q Rotate the array to right by 1 place
# def rotateArr(arr):
#     arr = [arr[(len(arr)-1)]] + arr[0:(len(arr)-1)]
#     return arr
# print(rotateArr([1,2,2,3,3,4,4,4]))
# def rotateArr(arr):
#     temp = arr[len(arr)-1]
#     for i in range(len(arr)-2,-1,-1):
#         arr[i+1] = arr[i]
#     arr[0] = temp
#     return arr
# print(rotateArr([1,2,2,3,3,4,4,4]))

#Q.Leetcode-189: Rotate an array by k places
#------------------Method 1---------------
# def rotateArrK(arr,K):
#     arr[:] = arr[(len(arr)-K):] + arr[:(len(arr)-K)]
#     return arr
#-------------------Method 2----------------
# def rotateArrK(arr, K):
#     n = len(arr)
#     K = K % n
#     temp = arr[n-K:]      # store last K
#     for i in range(n-K-1, -1, -1):
#         arr[i+K] = arr[i]
#     for i in range(K):
#         arr[i] = temp[i]
#     return arr
#--------------------Optimal-------------------
# def reverse(arr, start, end):                            #best solution
#     while start < end:
#         arr[start], arr[end] = arr[end], arr[start]
#         start += 1
#         end -= 1
# def rotateArrK(arr, K):
#     n = len(arr)
#     K = K % n   # handle K > n
#     # reverse entire array
#     reverse(arr, 0, n-1)
#     # reverse first K elements
#     reverse(arr, 0, K-1)
#     # reverse remaining elements
#     reverse(arr, K, n-1)
#     return arr

#Q.Leetcode-283: Move all zeroes to end in arr
# def moveZeros(arr):
#     for i in range(0,len(arr)):
#         if arr[i] == 0:
#             for j in range(i+1,len(arr)):
#                 if arr[j] != 0:
#                     arr[i],arr[j] = arr[j],arr[i]
#                     break
#     return arr
# print(moveZeros([1,2,0,4,6,7,0,0,0,3,4]))
#-------------------------optimal----------------------
# def moveZeros(arr):
#     pos = 0   # position for next non-zero
#     for i in range(0,len(arr)):
#         if arr[i] != 0:
#             arr[pos], arr[i] = arr[i], arr[pos]
#             pos += 1
#     return arr
# print(moveZeros([1,2,0,4,6,7,0,0,0,3,4]))


