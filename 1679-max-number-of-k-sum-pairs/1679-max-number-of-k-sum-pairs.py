class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        lowwer = 0
        higher = len(nums)-1
        no_operation = 0
        for i in range(len(nums)-1):
            Sum = nums[lowwer] + nums[higher]
            if Sum == k:
                lowwer += 1
                higher -= 1
                no_operation += 1
            elif Sum > k:
                higher -= 1
            else:
                lowwer += 1
            if lowwer >= higher:
                break
        return no_operation 
    
       
            
            