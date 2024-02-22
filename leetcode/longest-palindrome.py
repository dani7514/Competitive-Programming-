class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_counter = Counter(s)
       
        odd = 0
        result = 0
        for v in s_counter.values():
            if v % 2 == 0: 
                result += v
            else:
                odd = 1
                result += (v-1)
        
        return result + odd