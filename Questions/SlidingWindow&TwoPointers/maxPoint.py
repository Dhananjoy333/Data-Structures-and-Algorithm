#Q.Leetcode-1423 : given a number we can pick that many elements from array to get max substring but we must pick from end points
# def maxPoints(arr,num):
#     n = len(arr)
#     if n == num:
#         return sum(arr)
#     left_sum, right_sum = 0
#     for i in range(0,num):
#         left_sum  += arr[i]
#     maxi = left_sum
#     right_ind = n-1
#     for i in range(num-1,-1,-1):
#         left_sum -= arr[i]
#         right_sum += arr[right_ind]
#         maxi = max(maxi,left_sum + right_sum)
#         right_ind -= 1
#     return maxi 
 