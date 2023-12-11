class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        max_length_container = {}
        max_length = 1 

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                max_length += 1
            elif nums[i] != nums[i - 1]:
                max_length = 1

            max_length_container[max_length] = max(max_length, max_length_container.get(max_length, 0))

        return max(max_length_container.values(), default=1)

            