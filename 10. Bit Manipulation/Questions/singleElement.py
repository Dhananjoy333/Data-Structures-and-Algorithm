#Q. In a given array all elements are repeating except one output that element
def findSingle(arr):
    single = 0
    for i in arr:
        single = single ^ i
    return single
print(findSingle([5,6,7,8,9,6,8,7,5]))