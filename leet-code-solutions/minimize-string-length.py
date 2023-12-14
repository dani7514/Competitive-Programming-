class Solution:
    def minimizedStringLength(self, s: str) -> int:
        minimize_string = set()
        
        for char in s:
            minimize_string.add(char)
            
        return len(minimize_string)