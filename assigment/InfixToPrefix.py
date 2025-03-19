
class InfixToPrefix:
    def __init__(self, expression):
        self.expression = expression
    
    def precedence(self, op):
        if op == '+' or op == '-':
            return 1
        if op == '*' or op == '/':
            return 2
        if op == '^':
            return 3
        return 0

    def is_operator(self, c):
        return c in {'+', '-', '*', '/', '^'}
    
    def reverse_expression(self, expr):
        return expr[::-1].replace('(', 'temp').replace(')', '(').replace('temp', ')')
    
    def convert(self):
        expression = self.reverse_expression(self.expression)
        stack = []
        prefix = []
        
        for char in expression:
            if char.isalnum():  
                prefix.append(char)
            elif char == '(': 
                stack.append(char)
            elif char == ')':  
                while stack and stack[-1] != '(':
                    prefix.append(stack.pop())
                stack.pop()
            else:  
                while stack and self.precedence(stack[-1]) >= self.precedence(char):
                    prefix.append(stack.pop())
                stack.append(char)
        
        while stack:
            prefix.append(stack.pop())
        
        return ''.join(self.reverse_expression(''.join(prefix)))


infix_expr = "(A-B/C)*(A/K-L)"
converter = InfixToPrefix(infix_expr)
prefix_expr = converter.convert()
print("Prefix Expression:", prefix_expr)


