class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        num_zeros = nums.count(0)
        num_ones = nums.count(1)

        num_zeros_inLeft = 0
        num_ones_inLeft = 0
        score = []

        for i in range(len(nums)+ 1):
            if i == 0:
                if nums[i] == 0:
                    num_zeros_inLeft += 1
                else:
                     num_ones_inLeft += 1
    
                score.append(num_ones)
            elif i == len(nums):
                score.append(num_zeros)
            else:
                if nums[i] == 0:
                    num_ones_inRight = num_ones - num_ones_inLeft
                    temp_sum =  num_zeros_inLeft +  num_ones_inRight
                    score.append(temp_sum)
                    num_zeros_inLeft += 1
                    
                else:
                    num_ones_inRight = num_ones - num_ones_inLeft
                    temp_sum =  num_zeros_inLeft + num_ones_inRight
                    score.append(temp_sum)
                    num_ones_inLeft += 1
    
        max_score = max(score)
        result = []

        for i in range(len(score)):
            if score[i] == max_score:
                result.append(i)
        
        return result