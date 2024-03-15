class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low,high=0,len(nums)-1
        exist=False
        index=0
        while low <=high:
            mid= low + ((high - low)//2)
            index=mid
            if nums[mid]<target:
                low=mid+1    
            elif nums[mid]>target:
                high=mid-1
            else:
                exist=True
                break
        if exist:
            return index
        else:
            return low

            
            