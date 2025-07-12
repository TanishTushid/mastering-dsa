class Solution:
    def precedence(self, ch):
        if ch == '+' or ch == '-':
            return 1
        if ch == '*' or ch == '/':
            return 2
        if ch == '^':
            return 3
        return 0

    def infixtopostfix(self, s):
        stack = []
        result = []

        for char in s:
            if char.isalnum():  # Operand
                result.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    result.append(stack.pop())
                stack.pop()  # Remove '('
            else:  # Operator
                while stack and self.precedence(stack[-1]) >= self.precedence(char):
                    result.append(stack.pop())
                stack.append(char)

        # Pop any remaining operators
        while stack:
            result.append(stack.pop())

        return ''.join(result)

s = Solution()
print(s.infixtopostfix("A+B*C"))   # Output: ABC*+
print(s.infixtopostfix("(A+B)*C")) # Output: AB+C*
