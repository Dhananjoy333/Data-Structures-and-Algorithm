#Q. From given array of coins find minimum no. of coin to pick to get val
def minimumCoin(coins,val):
    coins.sort(reverse = True)
    print(coins)
    ans = []
    for i in range (0,len(coins)):
        if coins[i] == val :
            ans.append(coins[i])
            break
        elif coins[i] > val:
            continue
        else:
            while val - coins[i] >= 0:
                ans.append(coins[i])
                val = val - coins[i]
    return ans
print(minimumCoin([50,100,20,200,10,500,2,2000,1,5],47))

def minimumCoin(coins,val):
    coins.sort(reverse=True)
    ans = []
    for coin in coins:
        count = val // coin
        ans.extend([coin]*count)
        val -= coin*count
    return ans

print(minimumCoin([50,100,20,200,10,500,2,2000,1,5],47))