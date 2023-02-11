class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        
        max_num = 0 

        for i in range(len(nums)):
            left =  nums[:i]
            right = nums[i:]

            first_left_max = self.find_max_subarray(left,firstLen) + self.find_max_subarray(right,secondLen)

            second_left_max = self.find_max_subarray(left,secondLen) + self.find_max_subarray(right,firstLen)

            max_num = max(max_num, first_left_max, second_left_max)

        return max_num


    def find_max_subarray(self, nums, length):
        start = 0 
        end = 0
        n = len(nums)
        max_sum = 0
        sums = 0

        while end < n:
            sums += nums[end]
            length -= 1
            while length < 0 :
                sums -= nums[start]
                length += 1
                start += 1


            max_sum = max(max_sum, sums)
            end += 1
        return max_sum