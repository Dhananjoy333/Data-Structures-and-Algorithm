
#Q.Leetcode-904 : Fruit in basket, given two basket which can only take 1 type of fruit how many maximum fruit can both basket take
#-------------------------brute---------------------
# def Fbasket(arr):
#     n = len(arr)
#     maxi = 0
#     for i in range(0,n):
#         basket = set()
#         for j in range(i,n):
#             basket.add(arr[j])
#             if len(basket) < 3:
#                 maxi = max(maxi,j-i+1)
#             else:
#                 break
#     return maxi
# print(Fbasket([3,3,3,1,2,1,1,2,3,3,4]))
# #-------------------------better---------------------
# def Fbasket(arr):
#     maxi = 0
#     my_dict = {}
#     left = 0
#     right = 0
#     n = len(arr)
#     while right < n:
#         my_dict[arr[right]] = my_dict.get(arr[right],0) + 1
#         while len(my_dict)>2:
#             my_dict[arr[left]] -= 1
#             if my_dict[arr[left]] == 0:
#                 del my_dict[arr[left]]
#             left += 1
#         if len(my_dict) <= 2:
#             maxi = max(maxi, right - left +1)
#         right += 1
#     return maxi
# #-------------------------optimal---------------------
# def Fbasket(arr):
#     maxi = 0
#     my_dict = {}
#     left = 0
#     right = 0
#     n = len(arr)
#     while right < n:
#         my_dict[arr[right]] = my_dict.get(arr[right],0) + 1
#         if len(my_dict)>2:
#             my_dict[arr[left]] -= 1
#             if my_dict[arr[left]] == 0:
#                 del my_dict[arr[left]]
#             left += 1
#         if len(my_dict) <= 2:
#             maxi = max(maxi, right - left +1)
#         right += 1
#     return maxi