#Q. Leetcode-39 : find the combination sum to get target value we are allowed to repeat a value as many times as possible, also no duplicate value in given array
def combunationSum(arr,target):
    res = []
    def backtrack(ind,total,subset):
        if total == target:
            res.append(subset.copy())
            return
        if ind >= len(arr):
            return
        if total > target:
            return
        sum = total + arr[ind]
        subset.append(arr[ind])
        backtrack(ind,sum,subset)

        subset.pop()
        sum = total
        backtrack(ind + 1,sum, subset)
    backtrack(0,0,[])
    return res
print(combunationSum([2,3,4,7],7))