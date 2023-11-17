class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        j=0
        minl=float('inf')
        sumT=0
        while j<len(nums):
            sumT+=nums[j]
            while sumT>=target:
                minl=min(minl,j-i+1)
                sumT-=nums[i]
                i+=1
            j+=1
        if minl==float('inf'):
            return 0
        else:
            return minl
            
            
                
                
                       
        