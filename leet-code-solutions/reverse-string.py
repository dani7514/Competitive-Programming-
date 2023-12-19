class Solution:
    def reverseString(self, s: List[str]) -> None:
        end = len(s)-1
        start = 0

        while start <= end:
            s[start] , s[end] = s[end] , s[start]
            start += 1
            end -= 1
        