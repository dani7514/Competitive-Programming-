class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def possible(limit):
            cur = 1
            tmp = 0
            for i in weights:
                if i + tmp > limit:
                    cur += 1
                    tmp = i
                    if cur > days :
                        return False
                else:
                    tmp += i
            return True
                
        low = max(weights)
        high = sum(weights)
        ans = high
        while low <= high:
            mid = (low + high)//2
            if possible(mid):
                if mid < ans : ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
