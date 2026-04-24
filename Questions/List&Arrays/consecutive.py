#Q.Leetcode-128: Find the longest consecutive array sequence [1,99,101,98,2,5,3,100]  98,99,100,101-->4
# def consecutiveSeq(arr):                       #TC : O(N^2)
#     longestSeq = 1
#     hashMap = {}
#     for i in range(len(arr)):
#         hashMap[arr[i]] = i
#     for j in range(len(arr)):
#         i=j
#         temp = 1
#         while temp > 0:             
#             if (arr[i]+1) in hashMap:
#                 temp += 1
#                 i = hashMap[arr[i]+1]
#                 if (temp > longestSeq):
#                     longestSeq = temp
#             else :
#                 temp = -1
#     return longestSeq
# print(consecutiveSeq([1,99,101,98,2,5,3,100]))
#-----------------better-----------------
# def longestConsecutive(arr):              #TC : O(Nlog(N))
#     arr.sort()
#     longest = 0
#     count = 0
#     last_digit = float("-inf")
#     for i in range(len(arr)):
#         num = arr[i]
#         if (num-1 == last_digit):
#             count += 1
#             last_digit = num
#         elif(num != last_digit):
#             count = 1
#             last_digit = num
#         longest = max(longest,count)
#     return longest
# print(longestConsecutive([1,99,101,98,2,5,3,100,1,1,1]))
#----------------optimal------------------------
# def longestConsecutive(arr):                            #TC : O(N)
#     s = set(arr)
#     longest = 0
#     for num in s:
#         # start only if it's the beginning
#         if num - 1 not in s:
#             current = num
#             length = 1
#             while current + 1 in s:
#                 current += 1
#                 length += 1
#             longest = max(longest, length)
#     return longest
# print(longestConsecutive([1,99,101,98,2,5,3,100,1,1,1]))
arr = [1,99,101,98,2,5,3,100,1,1,1]
s = set(arr)
print(s)





    