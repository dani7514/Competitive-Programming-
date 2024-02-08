class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sum_t = 0
        sums = {0:1}
        count = 0
        
        for i in range(len(nums)):
            sum_t += nums[i]
            reminder = sum_t % k
            
            if reminder in sums:
                count += sums[reminder]
                
            if reminder in sums:
                sums[ reminder] += 1
            else:
                sums[reminder] = 1
             
        return count