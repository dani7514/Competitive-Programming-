class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        l = len(piles)
        return sum(piles[1:(l-l//3):2])

        