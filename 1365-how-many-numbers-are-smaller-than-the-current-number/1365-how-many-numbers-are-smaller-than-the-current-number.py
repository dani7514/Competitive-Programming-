class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        list=[0]*(len(nums))
        i=0
        while i<len(nums):
            for j in range(len(nums)):
                if nums[j]<nums[i]:
                    list[i]+=1
            i+=1
        return list
                
        