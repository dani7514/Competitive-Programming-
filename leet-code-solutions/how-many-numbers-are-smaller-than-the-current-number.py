class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        smaller_num_container = []
        not_sorted_num = [i for i in nums]
        nums.sort()

        for j in not_sorted_num:
            n=nums.index(j)
            smaller_num_container.append(n)
             
        return smaller_num_container
            
        