#There are different bitwise operators in Python. They are as follows:
#1. Bitwise AND (&)
#2. Bitwise OR (|) 
#3. Bitwise XOR (^)
#4. Bitwise NOT (~)
#5. Bitwise Left Shift (<<)
#6. Bitwise Right Shift (>>)

#----------------------------------And Operator----------------------------------
#The bitwise AND operator takes two binary numbers and performs a logical AND operation on each pair of corresponding bits. The result is 1 if both bits are 1, otherwise it is 0. For example:
a = 5  # In binary: 0101
b = 3  # In binary: 0011
c = a & b  # In binary: 0001, which is 1 in decimal
print(c)
#A pattern to remeber for AND operator is: 
#Step 1: Represent the numbers in addition of 1,2,4,8,16,32...
#Step 2: Find that is common, add all common numbers, that is the answer.
#Example: 13 = 1 + 4 + 8 , 7 = 1 + 2 + 4, common is 1 + 4 = 5, so 13 & 7 = 5

#----------------------------------Or Operator----------------------------------
# The bitwise OR operator takes two binary numbers and performs a logical OR operation on each pair of corresponding bits. The result is 1 if at least one of the bits is 1, otherwise it is 0. For example:
a = 5  # In binary: 0101
b = 3  # In binary: 0011
c = a | b  # In binary: 0111, which is 7 in decimal
print(c)
#A pattern to remeber for OR operator is: 
#Step 1: Represent the numbers in addition of 1,2,4,8,16,32...
#Step 2: Find that is common, add all common numbers along with remaining, that is the answer
# Example: 13 = 1 + 4 + 8 , 7 = 1 + 2 + 4, common is 1 + 4 = 5, remaining is 2 + 8 = 10, so 13 | 7 = 5 + 10 = 15

#----------------------------------Xor Operator----------------------------------
# The bitwise XOR operator takes two binary numbers and performs a logical exclusive OR operation on each pair of corresponding bits. The result is 1 if the bits are different, otherwise it is 0.
# Or Number of 1's is even ---> 0
# Or Number of 1's is odd ---> 1 
#  For example: 
a = 5  # In binary: 0101
b = 3  # In binary: 0011
c = a ^ b  # In binary: 0110, which is 6 in decimal
print(c)

#-----------------------------------Not Operator----------------------------------
# The bitwise NOT operator takes a single binary number and inverts all the bits. The result is 1 for every 0 bit and 0 for every 1 bit. For example:
a = 5  # In binary: 0101
c = ~a  # In binary: 1010, which is -6 in decimal (two's complement representation)
print(c)

#----------------------------------Left Shift Operator----------------------------------
# The bitwise left shift operator takes a binary number and shifts all the bits to the left by a specified number of positions. The vacated bits on the right are filled with 0s. For example:
a = 5  # In binary: 0101
c = a << 1  # In binary: 1010, which is 10 in decimal
print(c)
# The left shift operator is equivalent to multiplying the number by 2 for each shift. For example, shifting 5 to the left by 1 position (5 << 1) is equivalent to 5 * 2 = 10.
# x << n is equivalent to x * (2 ** n) for non-negative integers. For negative integers, the behavior of left shift can be implementation-dependent, but it generally performs a logical shift, which does not preserve the sign of the number.

#----------------------------------Right Shift Operator----------------------------------
# The bitwise right shift operator takes a binary number and shifts all the bits to the right by a specified number of positions. The vacated bits on the left are filled with 0s for unsigned numbers and with the sign bit for signed numbers. For example:
a = 5  # In binary: 0101
c = a >> 1  # In binary: 0010, which is 2 in decimal
print(c)
# The right shift operator is equivalent to dividing the number by 2 for each shift. For example, shifting 5 to the right by 1 position (5 >> 1) is equivalent to 5 // 2 = 2.
# x >> n is equivalent to x // (2 ** n) for non-negative integers. For negative integers, the behavior of right shift can be implementation-dependent, but it generally performs an arithmetic shift, which preserves the sign of the number.