class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        left_index_sum = {}
        right_index_sum = {}

        left_freq = {}
        right_freq = {}

        left_sum = [0] * len(nums)
        right_sum = [0] * len(nums)

        for i in range(len(nums)):
            
            if nums[i] in left_index_sum:
                left_sum[i] += (i * left_freq[nums[i]]) - left_index_sum[nums[i]]
                left_index_sum[nums[i]] += i
                left_freq[nums[i]] += 1
            else:
                left_index_sum[nums[i]] = i
                left_freq[nums[i]] = 1
    
        for i in range(len(nums)-1,-1,-1):
            if nums[i] in right_index_sum:
                right_sum[i] += right_index_sum[nums[i]] - (i * right_freq[nums[i]])
                right_index_sum[nums[i]] += i
                right_freq[nums[i]] += 1
            else:
                right_index_sum[nums[i]] = i
                right_freq[nums[i]] = 1

        for i in range(len(left_sum)):
            right_sum[i] += left_sum[i]

        return right_sum


