class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        freq_con = [0]* len(nums)
        
        for i, j in requests:
            freq_con[i] += 1
            if j + 1 < len(nums):
                freq_con[j+1] -= 1
        
        freq_con = list(accumulate(freq_con)) 
       
        freq_con.sort(reverse=True)
        nums.sort(reverse=True)



        result = 0
        for i in range(len(nums)):
            result += (nums[i] * freq_con[i])

        return result % (10**9 + 7)

        