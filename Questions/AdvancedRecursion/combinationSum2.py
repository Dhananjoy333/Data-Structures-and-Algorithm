#Q. Leetcode-40 : find the combination sum to get target value we are allowed to pick only once, also duplicate value exist in given array, result should not have duplicate array like [1,1,2]-->4 [1,2,1]-->4 only one should exist

def combinationSum2(arr,target):
    arr.sort()
    res = []
    def backtrack(ind, total,subset):
        if total == 0:
            res.append(subset.copy())
            return
        if total < 0:
            return
        if ind >= len(arr):
            return
        for i in range(ind,len(arr)):
            if i > ind and arr[i] == arr[i-1]:
                continue
            subset.append(arr[i])
            sum = total - arr[i]
            backtrack(i + 1,sum,subset)
            subset.pop()
    backtrack(0,target,[])
    return res
print(combinationSum2([1,1,1,2,2],4))

