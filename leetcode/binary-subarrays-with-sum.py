class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        temp_sum = 0
        temp_dict = {0:1}
        count = 0

        for i in nums:
            temp_sum += i
            diff = temp_sum - goal

            if diff in temp_dict:
                count += temp_dict[diff]

            if temp_sum in temp_dict:
                temp_dict[temp_sum] += 1
            else:
                 temp_dict[temp_sum] = 1
        
        return count