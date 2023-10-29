class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        k=set()
        t=set()
        
        for i in range(len(s)-9):
            temp=s[i: i+10]
    
            if temp in k:
                t.add(temp)
            else:
                k.add(temp)

        return list(t)
        