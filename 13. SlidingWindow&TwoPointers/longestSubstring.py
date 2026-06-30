#Q.Leetcode-3 : Longest substring without repetation
# def longestSub(s):
#     longest = 0
#     for i in range(len(s)):
#         hash = {}
#         count = 0
#         for j in range(i, len(s)):
#             if s[j] not in hash:
#                 hash[s[j]] = 1
#                 count += 1
#                 longest = max(longest, count)
#             else:
#                 break

#     return longest
# print(longestSub("dhananjoy"))
#----------------------------optimal----------------
# def longestSub(s):
#     n = len(s)
#     maxi = 0
#     my_dict = {}
#     left = 0
#     right = 0
#     while right < n:
#         if s[right] in my_dict:
#             left = max(left, my_dict[s[right]]+1)

#         maxi = max(maxi, right - left + 1)
#         my_dict[s[right]] = right
#         right += 1
#     return maxi
# print(longestSub("dhananjoy"))

