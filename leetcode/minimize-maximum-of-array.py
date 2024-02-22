class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        psum = nums
        
        for k in range(1, len(psum)):
            psum[k] = nums[k] + psum[k-1]

        sol = 0
        for k in range(len(psum)):
            if psum[k] % (k+1) != 0:
                sol = max((psum[k] // (k+1)) + 1, sol)
            else:
                sol = max(psum[k] // (k+1), sol)

        return sol
            