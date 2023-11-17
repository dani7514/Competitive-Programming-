class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        j=len(nums)-1
        arr=set()
        
        while i<j:
            avg=(nums[i]+nums[j])/2
            arr.add(avg)
            i+=1
            j-=1
        print(arr)
        return len(arr)
            
            
        