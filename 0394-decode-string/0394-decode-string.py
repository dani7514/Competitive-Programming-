class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        
        for i in range(len(s)):
            if s[i] !=']':
                stack.append(s[i])
            else:
                t=''
                while stack and stack[-1] != '[':
                    t = stack.pop() + t
                stack.pop()
                
                k=''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * t)
                
        return "".join(stack)
        