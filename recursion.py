#Recursion is a programming technique where a function calls itself in order to solve a problem. It typically involves a base case that stops the recursion and a recursive case that breaks the problem into smaller subproblems.

#Head recursion is a type of recursion where the recursive call is the first operation performed in the function. This means that the function will call itself before performing any other operations.
def head_recursion(n):
    if n == 0:
        return
    head_recursion(n - 1)
    print("Head Recursion:", n)   

#Tail recursion is a type of recursion where the recursive call is the last operation performed in the function. This means that the function will perform all its operations before calling itself.
def tail_recursion(n):
    if n == 0:
        return
    print("Tail Recursion:", n)
    tail_recursion(n - 1)
#Tail recursion is also known as backtracking because it allows the function to backtrack to previous states after reaching the base case.   

####################  Q.Find sum of n natural numbers using recursion.  ###############
#Parameterized recursion is a type of recursion where the function takes parameters that are modified in each recursive call. This allows the function to maintain state across recursive calls and can be used to solve problems that require more complex data structures.
def parameterized_recursion(sum,i,n):
    if i > n:
        print(sum)
        return
    parameterized_recursion(sum+i,i+1,n)

#Functional recursion is a type of recursion where the function is defined in terms of itself, often using higher-order functions or lambda functions. This allows for more flexible and expressive code, but can also lead to more complex and harder-to-understand code if not used carefully.
def functional_recursion(n):
    if n == 1:
        return 1
    return n + functional_recursion(n - 1)
    