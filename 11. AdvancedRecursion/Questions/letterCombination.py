#Q.Leetcode-17 : In a given letter-number keypad phone setup to get target value which combination of letters can be pressed
def letterCombination(val):
    res = []
    keypad = {"2" : "abc",
              "3" : "def",
              "4" : "ghi",
              "5" : "jkl",
              "6" : "mno",
              "7" : "pqrs",
              "8" : "tuv",
              "9" : "wxyz",}
    def backtrack(ind,subset):
        if ind >= len(val):
            res.append("".join(subset))
            return
        for i in keypad[val[ind]]:
            subset.append(i)
            backtrack(ind+1,subset)
            subset.pop()
    backtrack(0,[])
    print(res)
letterCombination("45")
            
