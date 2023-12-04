class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        i=0
        j=1
        arr=[]
        while j<len(nums):
            for _ in range(nums[i]):
                arr.append(nums[j])
            i+=2
            j+=2
        return arr