class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = reachable = 0
        for num in nums:
            while reachable < min(num - 1, n):
                reachable +=  reachable + 1
                patches += 1
            reachable += num
        
        while reachable < n:
            reachable = 2 * reachable + 1
            patches += 1 
        
        return patches