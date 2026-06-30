def subsequences(arr):
#     result = []
#     def backtrack(index,subset):
#         if index >= len(arr):
#             result.append(subset.copy())
#             return
#         #Include current element
#         subset.append(arr[index])
#         backtrack(index + 1, subset)
#         #Exclude current element
#         subset.pop()
#         backtrack(index + 1, subset)
#     backtrack(0,[])
#     return result
# print(subsequences([5,8,7]))