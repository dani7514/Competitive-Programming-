class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
    
        longer=max(len(word1),len(word2))
        st=""
        for i in range(longer):
            if i<len(word1):
                st+=word1[i]
            if i< len(word2):
                st+= word2[i]
        return st
        

        