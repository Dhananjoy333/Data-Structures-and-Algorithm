#Q. Given two numbers(start, goal) how many bit flips are required for start to become goal
def bitFlips(start, goal):
    res = start ^ goal 
    # doing XOR turn all required flips to 1 so now all we need to do is count the number of 1's 
    #ex start : 10(1010), goal : 7(0111), XOR : 1101 so 3 flips(0-1:1 ; 1-0:1; 1-1: 0; 0-0:1 so in XOR different becomes 1 same becomes 0)
    count = 0
    for i in range(0,32):
        if res & (1<<i) != 0:
            count += 1
    return count