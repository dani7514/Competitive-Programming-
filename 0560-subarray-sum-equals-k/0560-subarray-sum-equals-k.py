class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = 0
        sums = {0:1}
        count = 0
        for i in range(len(nums)):
            sum += nums[i]
            diff = sum - k
            
            if diff in sums:
                count += sums[diff]
                
            if sum in sums:
                sums[sum] += 1
            else:
                sums[sum] = 1
                
        return count
        