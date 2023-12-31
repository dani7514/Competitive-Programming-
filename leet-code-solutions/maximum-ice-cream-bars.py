class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        max_value = max(costs)
        freq_container = [0] * (max_value + 1)

        for i in costs:
            freq_container[i] += 1

        target = 0

        for index, value in enumerate(freq_container):
            for j in range(value):
                costs[target] = index
                target += 1
        
        sumT = 0
        result = 0

        for i in costs:
            sumT += i
            if sumT <= coins:
                result += 1
        
        return result