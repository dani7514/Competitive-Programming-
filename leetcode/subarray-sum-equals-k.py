class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_t = 0
        sums = {0:1}
        count = 0
        
        for i in range(len(nums)):
            sum_t += nums[i]
            diff = sum_t - k
            
            if diff in sums:
                count += sums[diff]
                
            if sum_t in sums:
                sums[sum_t] += 1
            else:
                sums[sum_t] = 1
                
        return count
        