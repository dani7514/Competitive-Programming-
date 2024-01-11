class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # brutforce code 
        
        # total = []

        # for i in range(len(nums)-1):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             total.append(nums[i]+nums[j]+nums[k])
        
        # final = {}
        # for i in range(len(total)):
        #     final[abs(target - total[i])] = total[i]
       
        # t = sorted(final.items())
        
        # return t[0][1]

        nums.sort()
        result = 0
        cur_diff = float("inf")

        for start in range(len(nums)-2):
            second = start + 1
            end = len(nums) - 1

            while second < end:
                cur_sum = nums[start] + nums [second] + nums[end]

                if abs(target - cur_sum) < cur_diff:
                    result = cur_sum
                    cur_diff = abs(target - cur_sum)

                elif cur_sum < target:
                    second += 1

                else:
                    end -= 1

        return result 

