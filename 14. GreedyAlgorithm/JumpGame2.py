#Leetcode-45 : In an array with num you can jump max upto that number. What is the minimum number of jumps to reach end
#-----------------------------------------Brute Force ------------------------------------
# def jumpGame2(arr):
#     def func(ind,jump):
#         if ind >= len(arr):
#             return jump
#         min_jump = float('inf')
#         for i in range(1,arr[ind]+1):
#             min_jump = min(min_jump,func(ind+i,jump + 1))
#         return min_jump
#     return func(0,0)
# print(jumpGame2([2,3,1,1,4]))

#------------------------------------------ Optimal --------------------------------------------
def jumpGame2(arr):
    jumps = 0
    left = 0
    right = 0
    while right < len(arr)-1:
        farthest = 0
        for i in range(left, right+1):
            farthest = max(farthest, i + arr[i])
        left = right + 1
        right = farthest
        jumps += 1
    return jumps
print(jumpGame2([2,3,1,1,4]))
