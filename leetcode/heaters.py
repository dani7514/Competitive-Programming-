class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()

        result = []

        for i in houses:
            idx = bisect.bisect_left(heaters,i)

            if 0 < idx < len(heaters):
                result.append(min(i-heaters[idx-1],heaters[idx]-i))
            elif idx == 0:
                result.append(heaters[idx]-i)
            else:
                result.append(i-heaters[-1])

        return max(result)