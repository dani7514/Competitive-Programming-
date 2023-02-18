class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "/": operator.truediv,
            "*": operator.mul
        }
        
        for token in tokens:
            if token in ops:
                y = stack.pop()
                x = stack.pop()
                stack.append(int(ops[token](x, y)))
            else:
                stack.append(int(token))
        return stack.pop()
        