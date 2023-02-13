class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        poper=0
        maxLength = 0
        usedChar = []
        
        for i in range(len(s)):
            
            while (s[i] in usedChar) :
                usedChar.remove(s[poper])
                poper+=1
                print(poper)
          
            maxLength = max(maxLength, i-poper + 1)
            usedChar.append(s[i])
            print(usedChar)
            

        return maxLength
        