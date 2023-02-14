class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum=0
        leftSum=0
        for i in nums:
            totalSum+=i
        for i in range(len(nums)):
            totalSum=totalSum-nums[i]
            if totalSum==leftSum:
                return i
            else:
                leftSum+=nums[i]
        return -1
        