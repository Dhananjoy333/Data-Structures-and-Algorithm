# arr=[6,7,9,5,4,12,45,6,1,2,3]
# l = len(arr)
# for i in range(0,l):
#     swapped = False
#     for j in range(0, l-1):
#         if arr[j+1] < arr[j]:
#             arr[j+1],arr[j] = arr[j], arr[j+1]
#             swapped = True
#         if not swapped:
#             break
#     l -= 1
# print(arr)

# #or
# def bubbleSort(arr):
#     n = len(arr)
#     for i in range(n):
#         swapped = False
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#                 swapped = True
#         if not swapped:
#             break

#Here the larget number is sent to last so sorting happen from backside ,as last element get sorted we dont need to check/loop last element hence n-i-1
#Time complexity is O(N^2)

    