class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left, right = 0, 0
        sub_array = set()
        sum_subarray = 0
        result = 0
        
        while right < len(nums):
            if nums[right] not in sub_array:
                sub_array.add(nums[right])
                sum_subarray += nums[right]
                right += 1
            
            else:
                sum_subarray -= nums[left]
                sub_array.remove(nums[left])
                left += 1
            
            result = max(result,sum_subarray)
            
        return result