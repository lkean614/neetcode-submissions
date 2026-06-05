class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operate = {'+','-','*','/'}
        for token in tokens:
            if token in operate:
                match token:
                    case '+':
                        ans = stack.pop() + stack.pop()
                    case '-':
                        a = stack.pop()
                        b = stack.pop()
                        ans = b - a
                    case '*':
                        ans = stack.pop() * stack.pop()
                    case _:
                        a = stack.pop()
                        b = stack.pop()
                        ans = int(b / a)
                stack.append(ans)    
            else:
                stack.append(int(token))
        return stack.pop()