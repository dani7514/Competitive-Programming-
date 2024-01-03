class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)>1:
            right=1;
            left=0
            while right<len(nums):
                if nums[right]==nums[left]:
                    nums.pop(right)
                else:
                    right+=1
                    left+=1
            return len(nums)
        return 1
            
            
       
            
            
        