class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        start = 0
        slicer=  2
        max_perimeter=0
        
        #iterating to get largest perimeter of a triangle 
        while slicer < len(nums):
            temporary = nums[start : slicer + 1]
            side_1=temporary[0]
            side_2=temporary[1]
            side_3=temporary[2]
            
            # check the those side make the triangle 
            if side_1 + side_2 > side_3 and side_1 + side_3 > side_2 and side_3 + side_2 > side_1:
                temp_perimeter = side_1 +  side_2 + side_3
                max_perimeter= max(max_perimeter, temp_perimeter)
                
            start += 1
            slicer += 1
                
        return max_perimeter 
        
        
        
