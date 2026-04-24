#Leetcode-55 : In an array with num you can jump max upto that number check if we can reach till end by jumps
def jumps(arr):
    max_ind = 0
    for i in range(0,len(arr)):
        if i > max_ind:
            return False
        max_ind = max(max_ind,i + arr[i])
    return True
print(jumps([3,2,1,2,0,2,1,5]))