class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        answer = 0

        for i in range(2, len(nums)):
            start, end = 0, i - 1
            while start < end:
                if nums[start] + nums[end] > nums[i]:
                    answer = answer + (end - start)
                    end = end - 1
                else:
                    start = start + 1

        return answer