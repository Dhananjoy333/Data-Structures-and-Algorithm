#Q. Swap numbers with bit manipulation (XOR)
# def swap(a,b):
#     a = a ^ b
#     b = a ^ b # XOR of same number is 0 so (a^b)^b = a
#     a = a ^ b
#     print(a,b)
# swap(3,4) 

# Set means to turn to 1 and clear means to turn to 0
#Q. Check if ith bit is set or not(i.e, ith bit is 1 or not)
# def bitCheck(a,i):
#     if a & (1<<i) != 0:
#         print(True)
#     else:
#         print(False)
# def bitCheck(a,i):
#     if (a>>i) & 1 != 0:
#         print(True)
#     else:
#         print(False)
# bitCheck(13,3)

#Q. Set the ith bit 
# def setBit(a,i):
#     res = a | (1<<i)
#     print(res)
# setBit(9,2)

#Q. Clear the ith bit
# def clearBit(a,i):
#     flip = ~(1<<i) #Not operator turns 1 to 0 and 0 to 1 so here flip = ....1011
#     res = a & flip
#     print(res)
# clearBit(13,2)

#Q. Toggle the ith bit
# def toggleBit(a,i):
#     res = a ^ (1<<i)
#     print(res)
# toggleBit(13,1)

#Q. Remove the last set bit (right-most)
# def removeSet(a):
#     res = a & (a-1)
#     print(res)
# removeSet(40)

#Q. Check if the number is power of 2
def checkPower(a):
    if a & (a-1) == 0:
        print(True)
    else:
        print(False)
checkPower(321)