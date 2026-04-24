#Q.Leetcode-121: Array elements show stock prices find max profit possible
# def buyAndSell(arr):                       #TC = O(N)
#     temp = 0
#     max = 0
#     for i in range(0,len(arr)):
#         temp = 0
#         for j in range(i,len(arr)):
#             if(arr[j] > arr[i]):
#                 temp = arr[j] - arr[i]
#                 if(temp > max):
#                     max = temp
#     return max if max>0 else 0
# print(buyAndSell([7,2,1,5,6,4,8]))           
#-----------------------optimal----------------------
# def buyAndSell(arr):                         #TC = O(N)
#     min_price = float('inf')
#     max_profit = 0
#     for i in range(len(arr)):
#         temp_profit = 0
#         if(arr[i] < min_price):
#             min_price = arr[i]
#         else:
#             temp_profit = arr[i]-min_price
#             if (temp_profit > max_profit):
#                 max_profit = temp_profit
#     return max_profit if max_profit>0 else 0
# print(buyAndSell([8,7,6,5,4])) 
# def buyAndSell(arr):
#     min_price = float('inf')
#     max_profit = 0

#     for price in arr:
#         min_price = min(min_price, price)
#         max_profit = max(max_profit, price - min_price)

#     return max_profit

        
