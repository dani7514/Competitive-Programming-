class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        L = len(r)
        res = [False]*L
        for i in range(L):
            arr = sorted(nums[l[i]:r[i] + 1])
            diff = set()
            for j in range(len(arr) - 1):
                diff.add(abs(arr[j + 1]  - arr[j]))
            if len(diff) == 1: res[i] = True
        return res
        