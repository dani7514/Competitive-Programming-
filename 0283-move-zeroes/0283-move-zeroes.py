class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        lf=0
        rg=1
        while rg < len(nums):
            if nums[lf]==0 and nums[rg]!=0:
                nums[lf],nums[rg]=nums[rg],nums[lf]
                lf+=1
                rg+=1
            elif nums[lf]==0 and nums[rg]==0:
                rg+=1
            else:
                lf+=1
                rg+=1
                
        
                
                