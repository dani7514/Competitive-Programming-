class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        arr1 = nums[:-3]
        arr2 = nums[3:]
        arr3 = nums[1:-2]
        arr4 = nums[2:-1]
        return min(arr1[-1] - arr1[0], arr2[-1] - arr2[0], arr3[-1] - arr3[0], arr4[-1] - arr4[0])