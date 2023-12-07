class Solution:
    def largestOddNumber(self, num: str) -> str:
        last_index = len(num)-1
        
        for i in range(last_index, -1, -1):
            if int(num[i]) % 2 != 0:
                return num[:i+1]
        return ""