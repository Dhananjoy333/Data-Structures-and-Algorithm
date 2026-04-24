def missingVal(arr):
    n = len(arr)
    expected = n * (n + 1) // 2
    actual = sum(arr)
    return expected - actual
print(missingVal([9,6,4,2,3,5,7,0,1]))