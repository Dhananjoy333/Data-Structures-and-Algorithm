#Q.Find the frequency of a number from a given array
#we solve this by dictonary/frequency map
# def findFreq(arr,num):
#     freqMap = {}
#     for i in range(0,len(arr)):        #----> O(N)
#         if arr[i] in freqMap:          #----> O(1) in dictionary searching takes constant time it doesnot iterate 
#             freqMap[arr[i]] += 1       #----> O(1) changing value in dict is also direct
#         else:
#             freqMap[arr[i]] = 1        #----> O(1)
#     if num not in freqMap:             #----> O(1)
#         return 0
#     else:
#         return freqMap[num]            #----> O(1)

# # O(N) time complexity, for space comlexity in worse case if all value in arr is unique dict size will same as len(arr) so O(N)
# print(findFreq([3,4,5,5,5,6,7,1,1,12,3,1,4,1],122))  

############  Method 2  ##########
# def findfreq(arr):
#     freqMap = {}
#     for i in range(0,len(arr)):
#         freqMap[arr[i]] = freqMap.get(arr[i],0) + 1
#     print(freqMap)
# findfreq([3,4,5,5,5,6,7,1,1,12,3,1,4,1])

#freqMap.get(arr[i],0) ---> here .get(arr[i],0) here .get looks for arr[i] if it exist it returns its value if not return value 0 

