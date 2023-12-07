class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        added_space = ""
        i = 0
        j = 0
        while i < len(s):
            if j < len(spaces) and  i == spaces[j]:
                j += 1
                added_space += " "
            else:
                added_space += s[i]
                i += 1
                
        return added_space
                
            
            
        