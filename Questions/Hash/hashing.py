# Q.find how many times a num from arr2 shows up in arr1
# def findFreq(arr1,arr2):              #brute force approach
#     freqMap = {}
#     for i in range(0,len(arr2)):
#         total = 0
#         for j in range(0,len(arr1)):
#             if arr2[i] == arr1[j] :
#                 total += 1
#         freqMap[arr2[i]]= total
#     print(freqMap)
# findFreq([2,3,4,4,6],[1,2,3,4,5,6])     #O(M * N)
# 
# if we know arr1 is from 1 to 10 i.e, 1<arr[i]<10
# def findFreq(arr1,arr2):
#     hashList = [0] * 11
#     hashMap = {}
#     for i in arr1:
#         hashList[i] += 1
#     for j in arr2:
#         if j < 1 or j > 10:
#             hashMap[j] = 0
#         else:
#             hashMap[j] = hashList[j]
#     print(hashMap)
# findFreq([2,3,4,4,6],[1,2,3,4,5,6,10,67,-2])    #O(M + N)

#if arr1 is not provided like 1<arr[i]<10 
# def findFreq(arr1,arr2):
#     freqMap1 = {}
#     solMap = {}
#     for i in range(0,len(arr1)):
#         freqMap1[arr1[i]] = freqMap1.get(arr1[i],0) + 1
#     for j in arr2:
#         solMap[j] = freqMap1.get(j,0)
#     print(solMap)
# findFreq([2,3,4,4,6],[1,2,3,4,5,6,10,67,-2])     #O(M + N) but works everywhere