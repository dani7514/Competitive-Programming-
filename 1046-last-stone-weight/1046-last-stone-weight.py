class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for _ in range(len(stones)-1):
            stones.sort()
            stones = [stones.pop()-stones.pop()]+stones[:]
        return stones.pop()
        