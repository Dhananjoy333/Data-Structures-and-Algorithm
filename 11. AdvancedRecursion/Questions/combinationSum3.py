#Q. Leetcode-216 : From 1 to 9 create subset having elements N which sum upto target
def combinationSum3(N, target):
    res = []
    def backtrack(last,total,subset):
        if total == target and len(subset) == N:
            res.append(subset.copy())
            return
        if total > target and len(subset) > N:
            return
        for i in range(last,10):
            sum = total + i
            subset.append(i)
            backtrack(last+1, sum, subset)
            subset.pop()
    backtrack(1,0,[])
    print(res)
combinationSum3(2,8)