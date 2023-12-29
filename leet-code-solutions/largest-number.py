class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        to_string = []

        for number in nums:
           to_string.append(str(number))

        for i in range(len(to_string)):
            for j in range(i, len(to_string)):
                temp_1 = to_string[i] + to_string[j]
                temp_2 = to_string[j] + to_string[i]
        
                if int(temp_2) > int(temp_1):
                    to_string[i], to_string[j] = to_string[j], to_string[i]

        how_many_zeros = 0

        for i in range(len(to_string)):
            if nums[i] == 0:
                how_many_zeros += 1
                
            if how_many_zeros == len(nums):
                return "0"

        return "".join(to_string)

        
       