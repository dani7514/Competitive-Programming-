class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
            sa=[]
            val=0
            minlen=len(nums)+1
            for i in nums:
                sa.append(i)
                val+=i
                while val>=target:
                    val-=sa.pop(0)
                    minlen=min(minlen,len(sa)+1)
            if minlen>len(nums):
                return 0
            return minlen
        