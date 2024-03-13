class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + ((high - low) // 2)

            if nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1

        low_1 = 0
        high_1 = len(nums) - 1
        while low_1 <= high_1:
            mid = low_1 + ((high_1 - low_1) // 2)

            if nums[mid] <= target:
                low_1 = mid + 1
            else:
                high_1 = mid - 1
        
        if low <= high_1 and nums[low] == target and high_1 >= 0 and nums[high_1] == target:
            return [low, high_1]
        else:
            return [-1, -1]
