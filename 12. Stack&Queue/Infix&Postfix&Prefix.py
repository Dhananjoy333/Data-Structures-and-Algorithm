#---------------Operator/Operands---------------
#Operators are basically all signs we use to conduct calculation : +, -, *, /, ** etc
#Operands are the things on which we do the operations: a + b, 5 - 1, a-z;A-z;0-9

#---------------Priority----------------
#Simply which Operators are solved first i.e, BODMAS

#---------------Prefix-------------------
#If we use operators before operands like *+pq ; -mn etc
#It is used in LISP programming language and also in trees

#----------------Infix-------------------
#If operators are inbetween operands like x + y; a - b
#Used basically everywhere in all languages for calculations

#----------------Postfix-----------------
#If operators used after operands
#Used in stack based calculations pq+ ; mn-

class Solution:
    def precedence(self, ch):
        # Define operator precedence hierarchy
        if ch == "+" or ch == "-":
            return 1
        if ch == "*" or ch == "/":
            return 2
        if ch == "^":
            return 3
        return 0  # For non-operators like '(' and ')'

#------------------Infix to Postfix--------------------
    def InfixtoPostfix(self, s):
        stack = []    # Stack to help with operator ordering
        result = []   # To store the postfix expression

        for char in s:
            # If character is an operand, add it directly to result
            if ("a" <= char <= "z") or ("A" <= char <= "Z") or ("0" <= char <= "9"):
                result.append(char)
           
            # If character is '(', push it to the stack
            elif char == "(":
                stack.append(char)
           
            # If character is ')', pop until '(' is encountered
            elif char == ")":
                while stack and stack[-1] != "(":
                    result.append(stack.pop())
                stack.pop()  # Discard the '('
           
            # If character is an operator
            else:
                # Pop operators with higher or equal precedence
                while stack and self.precedence(stack[-1]) >= self.precedence(char):
                    result.append(stack.pop())
                stack.append(char)  # Push current operator

        # Pop remaining operators from the stack
        while stack:
            result.append(stack.pop())

        return "".join(result)  # Convert list to string

#--------------------Infix to Prefix------------------
#1.Reverse the infix
#2.Infix to postfix
#3.Reverse the answer
    def infixToPrefix(self, s):
        # Step 1: Reverse the infix expression
        s = s[::-1]

        # Step 2: Swap opening and closing parentheses
        s = s.replace("(", "temp").replace(")", "(").replace("temp", ")")

        stack = []
        result = []

        # Step 3: Modified infix to postfix algorithm
        for char in s:
            # If character is an operand, add it directly to result
            if ("a" <= char <= "z") or ("A" <= char <= "Z") or ("0" <= char <= "9"):
                result.append(char)
           
            # If character is '(', push it to the stack
            elif char == "(":
                stack.append(char)
           
            # If character is ')', pop until '(' is encountered
            elif char == ")":
                while stack and stack[-1] != "(":
                    result.append(stack.pop())
                stack.pop()  # Discard the '('
           
            # If character is an operator
            else:
                # Note the change to '>' from '>=' in the infix to postfix algorithm
                # This handles right-associativity properly
                while stack and self.precedence(stack[-1]) > self.precedence(char):
                    result.append(stack.pop())
                stack.append(char)  # Push current operator

        # Pop remaining operators from the stack
        while stack:
            result.append(stack.pop())

        # Step 4: Reverse the result to get prefix expression
        return "".join(result[::-1])
    
#---------------------Postfix to Infix---------------------------
class Solution:
    def postToInfix(self, s):
        # Stack to store operands or partial infix expressions
        stack = []

        for char in s:
            # If character is an operand (letter or digit), push it to the stack
            #.isalnum() is same as ("a" <= char <= "z") or ("A" <= char <= "Z") or ("0" <= char <= "9")
            if char.isalnum():
                stack.append(char)
            else:
                # If character is an operator, pop two operands
                operand2 = stack.pop()  # Second operand (popped first)
                operand1 = stack.pop()  # First operand (popped second)

                # Combine operands with the operator, surrounded by parentheses
                new_expr = f"({operand1}{char}{operand2})"

                # Push the resulting expression back onto the stack
                stack.append(new_expr)

        # The final element in the stack is the complete infix expression
        return stack[-1]

#-------------------------Prefix to Infix-----------------------
class Solution:
    def preToInfix(self, s):
        # Stack to store operands or partial infix expressions
        stack = []

        # Process the prefix expression from right to left
        for char in s[::-1]:
            # If character is an operand (letter or digit), push it to the stack
            if char.isalnum():
                stack.append(char)
            else:
                # If character is an operator, pop two operands
                operand1 = stack.pop()  # First operand
                operand2 = stack.pop()  # Second operand

                # Combine operands with the operator, surrounded by parentheses
                new_expr = f"({operand1}{char}{operand2})"

                # Push the resulting expression back onto the stack
                stack.append(new_expr)

        # The final element in the stack is the complete infix expression
        return stack[-1]

#-----------------------------Postfix to Prefix---------------------   
class Solution:
    def postToPre(self, s):
        # Stack to store operands or partial prefix expressions
        stack = []

        # Process each character in postfix expression
        for char in s:
            # If the character is an operand, push it to the stack
            if char.isalnum():
                stack.append(char)
            else:
                # Pop two operands from the stack
                operand2 = stack.pop()  # Second operand (popped first)
                operand1 = stack.pop()  # First operand (popped second)

                # Combine the operands with the operator in prefix form
                new_expr = f"{char}{operand1}{operand2}"

                # Push the result back onto the stack
                stack.append(new_expr)

        # The final element in the stack is the prefix expression
        return stack[-1]

#-------------------------Prefix to Postfix-------------------------  
class Solution:
    def preToPost(self, s):
        # Stack to store operands or partial postfix expressions
        stack = []

        # Traverse the prefix expression from right to left using index
        n = len(s)
        for i in range(n - 1, -1, -1):  # Reverse iteration using index
            char = s[i]

            # If the character is an operand, push it to the stack
            if char.isalnum():
                stack.append(char)
            else:
                # Pop two operands from the stack
                operand1 = stack.pop()  # First operand
                operand2 = stack.pop()  # Second operand

                # Combine the operands with the operator in postfix form
                new_expr = operand1 + operand2 + char

                # Push the result back onto the stack
                stack.append(new_expr)

        # The final element in the stack is the postfix expression
        return stack[-1]
 