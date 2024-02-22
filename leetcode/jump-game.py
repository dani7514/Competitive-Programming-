class Solution:
    def canJump(self, nums: List[int]) -> bool:
        update = len(nums) - 1

        for i in range(len(nums)-2,-1,-1):
            dif = update - i
            if dif <= nums[i]:
                update = i
        if update == 0:
            return True
        else:
            return False