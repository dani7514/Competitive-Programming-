class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minL=float("inf")
        j=0
        tempSum=0
        for i in range(len(nums)):
            tempSum += nums[i]
            while tempSum>=target:
                minL=min(minL,i-j+1)
                tempSum-=nums[j]
                j+=1
        if minL == float("inf"):
            return 0
        return minL
                       
        