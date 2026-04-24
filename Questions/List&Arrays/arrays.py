#Q. Find the largest element in an array
# def largestEle(arr):
#     largest = arr[0]   #largest = 0 is bad because if all elements are negative largest never update
#     for i in arr:
#         if (i>largest):
#             largest = i
#     return largest
# print(largestEle([55,32,-99,99,3,69]))

#Q. Find the second largest element in the array
# def secondLar(arr):
#     largest = arr[0]
#     for i in arr:
#         if i > largest :
#             largest = i
#     secondLargest = float("-inf")
#     for i in arr:
#         if i != largest and i > secondLargest:
#             secondLargest = i
#     return None if secondLargest==float("-inf") else secondLargest
# # print(secondLar([55,32,-99,99,3,69]))
# print(secondLar([99,96,1,2,3,34]))
#---------------------------------optimal--------------------------------------
# def secondLar(arr):                              
#     largest = arr[0] 
#     second_largest = float("-inf")
#     for x in arr[1:]:
#         if x > largest:
#             second_largest = largest
#             largest = x
#         elif x < largest and x > second_largest:
#             second_largest = x

#Q. check if array is sorted or not
# def checkSorted(arr):
#     sorted = True
#     for i in range(1,len(arr)):
#         if (arr[i-1] > arr[i]):
#             sorted = False
#             break
#     return sorted
# print(checkSorted([1,2,3,4,5,6,7,4]))

#Q. Remove duplicate from sorted array (in place)
# def removeDup(arr):                     
#     newArr = []
#     for i in range(1,len(arr)):
#         if (arr[i] != arr[i-1]):
#             newArr.append(arr[i])
#     if (arr[0] != newArr[0]):
#         newArr.insert(0,arr[0])
#     arr = newArr
#     return len(arr)
#--------------------------------------------Better----------------------------------
# def removeDup(arr):                          #not good worse TC:O(N) SC: O(N) worse because interviewer expect to not use hashmap
#     j=0
#     hashMap = {}
#     for i in arr:
#         hashMap[i] = hashMap.get(i,0) + 1
#     for i in hashMap:
#         arr[j] = i
#         j +=1
#     return j
#-------------------------------------------optimal----------------------------------
def removeDup(arr):                          #optimal TC: O(N) SC:O(1)
    if not arr:
        return 0
    j = 0  # index of last unique element
    for i in range(1, len(arr)):
        if arr[i] != arr[j]:
            j += 1
            arr[j] = arr[i]
    print(j)
    return arr # length of array without duplicates
print(removeDup([1,2,2,3,3,4,4,4]))


  

            



