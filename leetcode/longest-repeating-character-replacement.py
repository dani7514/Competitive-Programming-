class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic={}
        maxposibility=0
        left=0
        maxFrequency=0
        for i in range(len(s)):
            dic[s[i]]=1+ dic.get(s[i],0)
            maxFrequency=max(maxFrequency,dic[s[i]])
             
            while (i-left+1)-maxFrequency> k:
                dic[s[left]]-=1
                left+=1
            maxposibility=max(maxposibility,i-left+1)
        return maxposibility
            
        
        