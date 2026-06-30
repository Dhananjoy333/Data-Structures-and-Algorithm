#Q. Generate all binary strings and adjacent values of 1 should not be 1 i.e, 1,1,1;0,1,1;1,1,0 not allowed 
def binaryString(b):
    arr = ["0"]*b
    res = []
    def backtrack(index,flag,arr):
        if index >= len(arr):
            res.append("".join(arr))
            return
        arr[index] = "0"
        backtrack(index + 1, True,arr)
        if flag == True:
            arr[index] = "1"
            backtrack(index + 1, False,arr)
            arr[index] = "0"        
    backtrack(0,True,arr)
    return res
print(binaryString(3))
