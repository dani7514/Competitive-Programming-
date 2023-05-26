class Solution:
    def frequencySort(self, s: str) -> str:
        contain_in_s={}
        
        for i in s:
            if i not in contain_in_s :
                contain_in_s[i]=1
            else:
                contain_in_s[i]+=1
            
        result=dict(sorted(contain_in_s.items(),key=lambda x:x[-1] ,reverse=True))
        
        new_s=""
        for j in result:
            for _ in range(contain_in_s[j]):
                new_s+=j
        return new_s
            