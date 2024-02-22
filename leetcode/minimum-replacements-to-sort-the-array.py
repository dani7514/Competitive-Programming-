class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        prev = nums[-1]
        result = 0

        for i in range(len(nums)-2,-1,-1):
            if nums[i] > prev:
                temp = (nums[i] + prev - 1) // prev
                prev = nums[i] // temp
                result += temp  - 1
            else:
                prev = nums[i]
        return result 
