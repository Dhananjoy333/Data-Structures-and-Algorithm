#Q. Find factorial of a number using recursion.
# def factorial(n):
#     if n == 1 or n==0:
#         return 1
#     return n * factorial(n-1)
# print(factorial(5))

#Q. Reverse an array using recursion.
# def reverseArray(arr, l, r):
#     if l >= r:
#         return
#     arr[l], arr[r] = arr[r], arr[l]
#     reverseArray(arr, l + 1, r - 1)
# arr = [5,7,3,2,6,1,5,9]
# reverseArray(arr, 1, 5)
# print(arr)

#Q. Check if a string is palindrome
# def palindromeStr(Str,l,r):
#     if l >= r:
#         return True
#     if Str[l] != Str[r]:
#         return False
#     return palindromeStr(Str, l+1, r-1)
# string = "mom"
# print(palindromeStr(string,0,len(string)-1))

#Q. Give nth Fibonacci number
# def fibonacci(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     return (fibonacci(n-1)+fibonacci(n-2)) 
# print(fibonacci(5))



