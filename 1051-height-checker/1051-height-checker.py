class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        s=sorted(heights)
        return sum(heights[i] != s[i] for i in range(len(heights)))
            
            
            
        