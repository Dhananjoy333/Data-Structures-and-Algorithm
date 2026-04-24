#Q.Leetcode-2149: In an array there will be positive and negative numbers rearrage ain P and N consecutive order, start with positive
# def rearrange(nums):
#     positives = []
#     negatives = []
#     result = []
#     j = 0
#     for num in nums:
#         if num > 0:
#             positives.append(num)
#         else:
#             negatives.append(num)
#     while j < len(positives):
#         result.append(positives[j])
#         result.append(negatives[j])
#         j += 1
#     return result
# print(rearrange([-1,1]))
#------------------------------optimal-----------------------
# def rearrangeArray(nums):
#     res = [0] * len(nums)
#     pos, neg = 0, 1
#     for num in nums:
#         if num > 0:
#             res[pos] = num
#             pos += 2
#         else:
#             res[neg] = num
#             neg += 2
#     return res
