#Q. Given am array each having set with two value (value,weight) and given a weight fill upto weight maximising the value
#Hint : need to see max unit ratio

def fractionalknapsack(arr, wt):
    arr.sort(key =lambda x: x[0]/x[1], reverse = True)
    
    cur_value = 0
    max_weight = 0

    for i in range(0,len(arr)):
        if cur_value + arr[i][1] <= wt:
            cur_value += arr[i][1]
            max_weight += arr[i][0]
        else:
            remain = wt - cur_value
            cost = arr[i][0]/arr[i][1] * remain
            max_weight += cost
            break
    return max_weight  
x = [(160,10),(100,20),(200,50),(100,50)]
print(fractionalknapsack(x,90))