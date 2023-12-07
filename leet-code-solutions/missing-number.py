class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        temp_set = set()
        nums.sort()
        
        for i in nums:
            temp_set.add(i)
        
        for i in range(len(nums)+1):
            if i not in temp_set:
                return i
            
            