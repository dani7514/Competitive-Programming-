class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
            if sum(nums) < target :
                return 0

            low = 0
            ans = float("inf")
            tmp = 0

            for i in range(len(nums)) :
                tmp += nums[i]

                if tmp >= target :
                    while tmp - nums[low] >= target :
                        low += 1
                        tmp = tmp - nums[low-1] 
                    ans = min(ans, i-low+1)

            return ans
        