class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total = sum(arr[:k])
        res = int(total >= k * threshold)
        
        for i in range(k, len(arr)):
            total += arr[i] - arr[i-k]
            if total >= k * threshold:
                res += 1
        
        return res
        