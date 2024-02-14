class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if nums:
            summer = nums[0]
            maximum = nums[0]
        
            for i in range(1, len(nums)):
                summer = max(nums[i], summer + nums[i])
                maximum = max(maximum, summer)
            return maximum
    
        else: return -1
                
                
                
            
        