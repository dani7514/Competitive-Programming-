class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == len(cardPoints):
            return sum(cardPoints)
        
        suffix_sums = [0]*len(cardPoints)
        
        for i in range(len(cardPoints)-1, -1, -1):
            if i == len(cardPoints)-1:
                suffix_sums[i] = cardPoints[i]
            else:
                suffix_sums[i] = suffix_sums[i+1] + cardPoints[i]
        
        max_points = -float("Inf")
        sums = 0
        
        for i in range(min(k+1, len(cardPoints))):
            a = suffix_sums[-(k-i)] if (k-i) > 0 else 0
            max_points = max(max_points, sums + a)
            sums += cardPoints[i]
        
        return max_points
        