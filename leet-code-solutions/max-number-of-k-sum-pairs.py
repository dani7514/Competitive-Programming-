class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left=0
        right=len(nums)-1
        k_sum=0
        while left<right:
            tempSum=nums[left]+nums[right]
            if tempSum<k:
                left+=1
            elif tempSum==k:
                k_sum+=1
                left+=1
                right-=1    
            else:
                right-=1
        return k_sum