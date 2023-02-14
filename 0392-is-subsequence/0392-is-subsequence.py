class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointerforT=0
        count=0
        for i in range(len(t)):
            if pointerforT<len(s):
                if t[i] ==s[pointerforT]:
                    count+=1
                    pointerforT+=1
        if count==len(s):
            return True
        else: 
            return False
                    