class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        num_occur = n // 4

        for i in range(n - num_occur):
            if arr[i] == arr[i + num_occur]:
                return arr[i]

        
        