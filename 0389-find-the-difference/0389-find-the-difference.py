class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        con1={}
        con2={}
        add=0
        for i in range(len(t)):
            if i<len(s) and s[i] in con1:
                con1[s[i]]+=1
            elif i<len(s) and s[i] not in con1:
                con1[s[i]]=1
                
            if t[i] in con2:
                con2[t[i]]+=1
            else:
                con2[t[i]]=1
                
        for j in con2:
            if j in con1:
                if con1[j] <con2[j]:
                    add=j
            else:
                add=j
        return add
                
        
        