class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        k = 0
        temp = set()

        for i in nums:
            if i not in temp:
                k += 1
                temp.add(i)

        
        result = 0
        right = 0
        temp_set = set()
        for left in range(len(nums) - k + 1): 
            temp = 0
            
            while right < len(nums):
                if nums[right] not in temp_set:
                    temp += 1
                    temp_set.add(nums[right])

                if temp == k:
                    result += 1
                
                right += 1

            right = left + 1
            temp_set = set()

        return result


                         