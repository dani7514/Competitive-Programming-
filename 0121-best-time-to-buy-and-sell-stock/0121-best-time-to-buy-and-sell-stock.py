class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        i, j = 0, 1
        n = len(prices)

        while j < n:
            if prices[i] > prices[j]:
                i = j
            else:
                if maxi < prices[j] - prices[i]:
                    maxi = prices[j] - prices[i]
            j += 1         
        return maxi
        
        