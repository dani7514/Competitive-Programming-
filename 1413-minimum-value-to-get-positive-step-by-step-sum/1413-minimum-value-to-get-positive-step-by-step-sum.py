class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        for i in range(1,len(nums)):
            nums[i]=nums[i] +nums[i-1]
        if min(nums)<0:
            startValue=-1*(min(nums)) +1
            return startValue
        else:
            return 1