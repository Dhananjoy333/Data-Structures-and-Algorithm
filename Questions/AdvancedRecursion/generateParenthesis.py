#Q.Leetcode-22 : Generate valid parenthesis 
def parenthesis(num):
    res = []
    brackets = [""] * (num * 2)
    def solve(ind,total,bracket):
        if ind >= len(brackets):
            if total == 0:
                res.append("".join(brackets))
            return
        if total > len(brackets)//2 :
            return
        elif total < 0:
            return
        brackets[ind] = "("
        sum = total + 1
        solve(ind+1, sum, brackets)  

        brackets[ind] = ")"
        sum = total - 1
        solve(ind+1, sum, brackets) 
    solve(0,0,brackets)
    return res
print(parenthesis(4))