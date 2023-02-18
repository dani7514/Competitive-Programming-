class Solution:
    def reverseParentheses(self, s: str) -> str:
        auxS = list(s)
        sett = set(['(', ')'])
        def reverse(start, end):
            while start < end:
                while start < end and auxS[start] in sett:
                    start += 1
                while start < end and auxS[end] in sett:
                    end -= 1
                tmp = auxS[start]
                auxS[start] = auxS[end]
                auxS[end] = tmp
                start += 1
                end -= 1
        
        stack = []
        
        for i in range(len(auxS)):
            if auxS[i] == '(':
                stack.append(i)
            if auxS[i] == ')':
                reverse(stack.pop(), i)
        
        res = ''
        
        for i in range(len(auxS)):
            if auxS[i] not in sett:
                res += auxS[i]
        return res
        