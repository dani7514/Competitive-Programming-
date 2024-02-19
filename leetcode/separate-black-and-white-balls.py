class Solution:
    def minimumSteps(self, s: str) -> int:
        result = 0
        count_zero = 0

        for i in range(len(s)-1, -1, -1):
            if s[i] == "1":
                result += count_zero
            else:
                count_zero += 1

        return result 
