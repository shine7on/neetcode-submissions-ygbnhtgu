class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        operators = ['+', '-', '*', '/']

        for s in tokens:
            if s not in operators:
                stack.append(int(s))
            else:
                y = stack.pop()
                x = stack.pop()
                if s == '+':
                    stack.append(x+y)
                elif s == '-':
                    stack.append(x-y)
                elif s == '*':
                    stack.append(x*y)
                elif s == '/':
                    if y == 0:
                        return 0
                    stack.append(math.trunc(x/y))
        return stack.pop()
                
        