class solution:
    def postToinfix(self,s):
        stack = []

        for char in s:
            #if character is an operand, push it to the stack
            if char.isalnum():
                stack.append(char)
            else:
                #pop two operands
                operand2 = stack.pop()
                operand = stack.pop()

                #combine operands with the operator
                new_expr = f"({operand}{char}{operand2})"

                #push the result back onto the stack
                stack.append(new_expr)
        # the final element in the stack is the infix expression
        return stack[-1]    
    
s = solution()
print(s.postToinfix("AB-DE+F*/"))  
