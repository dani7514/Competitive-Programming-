class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        to_stop = len(piles) - (len(piles)//3)
        result = 0

        for i in range(1,to_stop,2):
            result += piles[i]

        return result
        