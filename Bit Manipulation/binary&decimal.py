#Converting decimal to binary
def decimal_to_binary(n):
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary[::-1]
#Converting binary to decimal
def binary_to_decimal(b):
    decimal = 0
    for i in range(len(b)):
        decimal += int(b[-(i + 1)]) * (2 ** i)
    return decimal
#Inside computer integers are usually given in 32 bits, 13 in binary is 1101, but in 32 bits it is represented as 00000000000000000000000000001101
#1's complement of a binary number is obtained by inverting all the bits, 0's become 1's and 1's become 0's. For example, the 1's complement of 1101 is 0010.
#2's complement of a binary number is obtained by adding 1 to the 1's complement. For example, the 2's complement of 1101 is 0010 + 1 = 0011.
#Complement of a binary number is used to represent negative numbers in binary. For example, the 2's complement of 13 (1101) is 0011, which represents -13 in binary. 2's complement is preferable to 1's complement because it has only one representation for zero (0000) and it simplifies the arithmetic operations.

# In 32 bits that is provided the last bit is the sign bit:
# 0 to +ve numbers
# 1 to -ve numbers 