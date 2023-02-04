class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        num=[]
        for i in range(len(nums) // 2):
            tmpSum=nums[i] + nums[len(nums) - 1 - i]
            num.append(tmpSum)
        return max(num)
            
       
        