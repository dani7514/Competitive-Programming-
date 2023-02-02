class Solution(object):
    def isValid(self, s):
        stack=[]
        dic={"}":"{",")":"(","]": "["}
        for i in s:
            if i in dic:
                if stack and stack[-1]==dic[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)  
        if not stack:
            return True
        else:
            return False
        
       
        
        