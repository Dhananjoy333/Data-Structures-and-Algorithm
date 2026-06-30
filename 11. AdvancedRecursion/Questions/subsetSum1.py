#Q. Retuen a list of sum value of all subsets formed
def subsetSum(arr):
    res = []
    def backtrack(ind,total):
        if ind >= len(arr):
            res.append(total)
            return
        sum = total + arr[ind]
        backtrack(ind+1,sum)
        sum = total
        backtrack(ind+1,sum)
    backtrack(0,0)
    return res
print(subsetSum([5,9,3]))
