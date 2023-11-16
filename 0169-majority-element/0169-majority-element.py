class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        container={}
        n=len(nums)
        major=0
        for i in nums:
            if i in container:
                container[i]+=1
            else:
                container[i]=1
        
        for j in container:
            if container[j]>(n/2) :
                major=j
        return major
                
        