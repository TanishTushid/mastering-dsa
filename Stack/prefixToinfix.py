class solution:
    def pretoinfix(self,s):
        stack = []

        for char in s[::-1]:
            if char.isalnum():
                stack.append(char)
            else:
                opr1 = stack.pop()
                opr2 = stack.pop()

                new_expr = f"({opr1}{char}{opr2})"
                stack.append(new_expr)

        return stack[-1]
    
s = solution()
print(s.pretoinfix("*+PQ-MN"))