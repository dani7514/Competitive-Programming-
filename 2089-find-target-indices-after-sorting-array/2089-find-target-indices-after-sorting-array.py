class Solution(object):
    def targetIndices(self, nums, target):
        swap=0
        for i in range(len(nums)-1):
            for j in range(len(nums)-1-i):
                if nums[j]>nums[j+1]:
                    swap+=1
                    nums[j],nums[j+1]=nums[j+1],nums[j]
            if swap==0:
                break
        index=[]
        for k in range(len(nums)):
            if nums[k]==target:
                index.append(k)
        return index