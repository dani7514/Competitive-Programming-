class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        result = 0

        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                result += len(nums) - (i+1)

        return result