
class solution:
    def postfixToprefix(self,s):
        # stack to store operand
        stack = []

        #process each character in postfix expression
        for char in s:
            # if the character is an operand, push it to the stack
            if char.isalnum():
                stack.append(char)
            else:
                # pop two operands from the stack
                opr1 = stack.pop()
                opr2 = stack.pop()

                #combine the operands with the operator in prefix form
                new_expr = f"{char}{opr1}{opr2}"

                # push the result back onto the stack
                stack.append(new_expr)

        # final element in the stack is the prefix expression
        return stack[-1]
    
s = solution()
print(s.postfixToprefix("AB-DE+F*/"))