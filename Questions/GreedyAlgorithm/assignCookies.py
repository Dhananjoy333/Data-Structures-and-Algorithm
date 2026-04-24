#Q. Leetcode-455 : given an array of children with some greed factor and another array with no. of cookies return the max number of children who can get cookie
def assignCookie(children,cookie):
    children.sort()
    cookie.sort()
    left = 0
    right = 0
    count = 0
    while left < len(children) and right < len(cookie):
        if children[left] <= cookie[right]:
            count += 1
            left += 1
        right += 1
    return count
print(assignCookie([2,6,8,1,4],[4,2,7,1,2,3]))