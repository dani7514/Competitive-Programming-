class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        index = 0
        result = ""
        while index < len(s):
            if len(s) - index >= k:
                result += s[index: index+k][::-1]
                index += k
            else:
                result += s[index: len(s)][::-1]
                index = len(s)
            
            if index<len(s):
                if len(s) - index >= k:
                    result += s[index: index+k]
                    index += k
                else:
                    result += s[index:len(s)]
                    index = len(s)
        return result