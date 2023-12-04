class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w=""
        for i in word1:
            w+=i
        w1=""
        for j in word2:
            w1+=j
        
        if w==w1:
            return True
        else:
            return False
        