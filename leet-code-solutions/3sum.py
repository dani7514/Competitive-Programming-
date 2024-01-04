class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        i = 0
        result = set()

        while i < len(nums) - 2:
            k = i + 1
            j = len(nums) - 1

            while k < j:
                temp = nums[i] + nums[j] + nums[k]
                if temp == 0:
                    result.add((nums[i] , nums[k], nums[j]))
                    j -= 1
                    k += 1
                elif temp < 0:
                    k += 1
                else:
                    j -= 1

            i += 1

        return result

