#Important patterns in recursion

#1. Print all the subsequences
#2. Find all subsequences with sum = k
#3. Check if there exist a subsequence with sum = k
#4. Count all subsequences with sum = k

#---------------------Print all subsequences-------------
def subsequences(arr):
    result = []
    def backtrack(index,subset):
        if index >= len(arr):
            result.append(subset.copy())
            return

        #Include current element
        subset.append(arr[index])
        backtrack(index + 1, subset)

        #Exclude current element
        subset.pop()
        backtrack(index + 1, subset)
    backtrack(0,[])
    return result
print(subsequences([5,8,7]))

#Note: Backtracking is a type of recursive function where 
# 1. You make a choice
# 2. You explore that choice
# 3. You undo the choice (go back)
# 4. Then try another choice
# In my code .pop() takes me back and i can take another choice. But in recursion like find factorial we just go forward this is not backtracking
#------------------------Find all subsequences with sum = k------------------
# def subsequences(arr, target_sum):
#     result = []    
#     def backtrack(index, subset, current_sum):
#         if index >= len(arr):
#             if current_sum == target_sum:
#                 result.append(subset.copy())
#                 return
#             elif current_sum > target_sum:
#                 return  
#             if index >= len(arr):
#                 return  
#     
#         # Include
#         subset.append(arr[index])
#         backtrack(index + 1, subset, current_sum + arr[index])   
#     
#         # Exclude
#         subset.pop()
#         backtrack(index + 1, subset, current_sum)   
#     backtrack(0, [], 0)
#     return result
# print(subsequences([5,9,3,4,1],9))
#------------------------Check if there exist a subsequence with sum = k------------------
# def subsequences(arr, target_sum):
#     result = []    
#     def backtrack(index, subset, current_sum):
#         if index >= len(arr):
#             if current_sum == target_sum:
#                 result.append(subset.copy())
#                 return True
#             elif current_sum > target_sum:
#                 return False  
#             if index >= len(arr):
#                 return False   
#   
#         # Include
#         subset.append(arr[index])
#         pick = backtrack(index + 1, subset, current_sum + arr[index])   
#         if pick == True:
#             return True    

#         # Exclude
#         subset.pop()
#         not_pick = backtrack(index + 1, subset, current_sum) 
#         return not_pick  
#     return backtrack(0, [], 0)
# print(subsequences([5,9,3,4,1],9))
#if question only ask to return True/False
# def subsequences(arr,target_sum):
#     def backtrack(index,total):
#         if total == target_sum:
#             return True
#         elif total> target_sum:
#             return False
#         if index >= len(arr):
#             return False

#         sum = total + arr[index]
#         pick = backtrack(index + 1, sum)
#         if pick == True:
#             return True

#         sum = total
#         not_pick = backtrack(index + 1, sum)
#         return not_pick
#     return backtrack(0,0)
# print(subsequences([5,9,3,4,1],9))

#-----------------------------Count all subsequences with sum = k---------------------

# def subsequences(arr,target_sum):
#     def backtrack(index,total):
#         if total == target_sum:
#             return 1
#         elif total> target_sum:
#             return 0
#         if index >= len(arr):
#             return 0
        
#         sum = total + arr[index]
#         pick = backtrack(index + 1, sum)

#         sum = total
#         not_pick = backtrack(index + 1, sum)
#         return pick + not_pick
#     return backtrack(0,0)
# print(subsequences([5,9,3,4,1],5))