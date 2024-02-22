class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        mistake = 0
        temp = 0
        for i in s:
            if i == "(":
                temp += 1
            elif i == ")":
                if temp > 0:
                    temp -= 1
                else:
                    mistake += 1

        return temp + mistake