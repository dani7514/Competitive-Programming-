class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        visited = set() 
        for i in range(len(nums)): 
            if i not in visited:
                cycle_set = set()
                while True:
                    if i in cycle_set:
                        return True
                    
                    visited.add(i)
                    cycle_set.add(i)
                    prev, i = i, (i + nums[i])% len(nums)
                    if prev == i :
                        break
                    
                    if nums[prev] > 0 != nums[i] < 0:
                        break
        return False