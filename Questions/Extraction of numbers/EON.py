#Extraction of digits
# x = 12345
# y = 0
# while x > 0 :
#     y = (y*10) + (x%10)
#     x = x // 10
# print(y)


#Q. Count the number of digits in a given integer num
# def countDigits(num):                                   #it has time complexity of O(log(n)) here digits gets decreased each time if 
#     no_of_digits = 0                                     digits get divided by 10 each time its O(log10(n)) if 5 O(log5(n))
#     while num > 0:
#         no_of_digits = no_of_digits + 1
#         num = num // 10    
#     return no_of_digits
# print(countDigits(102938000))
##################  other way ################
# import math
# def countDigits(num):
#     count = int(math.log10(num) + 1)
#     return count
# print(countDigits(1223500000))

# for string we can simply do 
# count = 0
# for _ in string:
#     count += 1


# Q.Palindrome : it is a type of number or string which seem same when read from both front side and abck side like 12321 or nitin
# def PalindromeCheck(num):
#     n = num
#     rev = 0
#     while n > 0:
#         rev = rev*10 + n%10
#         n = n//10
#     if num == rev :
#         return "it is palindrome"
#     return "it is not a palindrome"
# print(PalindromeCheck(123211))
# def PalindromeCheck(num):
#     n = num
#     rev = 0
#     while n > 0:
#         rev = rev *10 + n%10
#         n = n//10
#     return num == rev
# print(PalindromeCheck(123211))

# def PalindromeCheckStr(str):
#     s = str
#     left = 0
#     right = len(s)-1
#     while left < right :
#         if(s[left] != s[right]):
#             return "not a palindrome"
#         left += 1
#         right -= 1
#     return "it is palindrome"
# print(PalindromeCheckStr("nitin"))


# Q. Armstrong number : it is a type of number which when each digit is raised to number of digits and added gives back the same number for ex: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153 or 1634 = 1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634
# def armstrongCheck(num):                              Time complexity = O(log(n))
#     n = num 
#     check = num 
#     digits = 0
#     total = 0
#     while n > 0:
#         digits += 1
#         n = n//10
#     while check > 0 :
#         last_digit = check%10
#         total = total + last_digit**digits
#         check = check//10
#     return num == total
# print(armstrongCheck(1634))


#Q. Return the factors of a given number
# def findFactors(num):                            Time complexity O(n)
#     factors = []
#     for i in range(num):
#         if num%(i+1) == 0 :
#             factors.append(i+1)
#     return factors
# print(findFactors(20))

# optimsed
def findFactors(num):                                       #Time complexity O(root(n))
    factors = []
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            factors.append(i)          # first factor
            if i != num // i:          # avoid duplicate for perfect squares
                factors.append(num // i)  # paired factor
    return sorted(factors)

print(findFactors(20))

