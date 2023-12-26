class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        max = 0
        count = 0

        for i in range(len(flips)):
            if max < flips[i]:
                max= flips[i]
            if max == i+1:
                count += 1
                
        return count