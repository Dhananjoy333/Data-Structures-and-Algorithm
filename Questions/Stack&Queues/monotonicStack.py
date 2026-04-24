#Q. Next greater element if none return -1
# def nextGreater(arr):
#     res = [-1] * len(arr)
#     if len(arr) == 0 or len(arr) == 1:
#         return res
#     for i in range(0,len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[j] > arr[i]:
#                 res[i] = arr[j]
#                 break
#     return res
# print(nextGreater([19,4,2,11,6,5,3,10]))
#------------------optimal--------------------
#Monotonic stack is simply a stack which stores elements in some order either ascending or descending
# def nextGreater(arr):
#     res = [-1] * len(arr)
#     stack = []
#     for i in range(len(arr)-1,-1,-1):
#         while len(stack) != 0 and stack[-1] <= arr[i]:
#             stack.pop()
#         if len(stack) != 0:
#             res[i] = stack[-1]
#         stack.append(arr[i])
#     return res
# print(nextGreater([19,4,2,11,6,5,3,10]))

# #Q.Leetcode-503 : Next Greater element 2
# def nextGreater2(arr):
#     n = len(arr)
#     res = [-1] *n
#     stack = []
#     for i in range(2*n-1,-1,-1):
#         while len(stack) != 0 and stack[-1] <= arr[i%n]:
#             stack.pop()
#         if i < n:
#             if len(stack) != 0:
#                 res[i] = stack[-1]
#         stack.append(i%n)
#     return res 

# Q.Leetcode-735 : Asteroid collision
def asteroidCol(arr):
    stack = []
    for i in range(0,len(arr)):
        if arr[i] > 0:
            stack.append(arr[i])
        else:
            while len(stack) != 0 and stack[-1]>0 and stack[-1] < abs(arr[i]):
                stack.pop()
            if len(stack) != 0 and stack[-1] == abs(arr[i]):
                stack.pop()
            elif len(stack) == 0 or stack[-1] < 0:
                stack.append(arr[i])
    return stack
print(asteroidCol([4,7,1,1,2,-3,-7,17,15,-18,-19]))
              
                

