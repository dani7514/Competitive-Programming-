class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        n = len(nums)
        dic = dict()
        for i in range(n):
            dic[nums[i]] = i
        pairs = set()
        for i in range(n):
            x = nums[i]
            for y in (x-k, x+k):
                if y in dic and i != dic[y]:
                    pairs.add(tuple(sorted((x, y))))
        return len(pairs)
                
                
                
                