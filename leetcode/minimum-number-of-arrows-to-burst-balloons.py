class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort()
        prev = points[0]
        res = 1

        for i  in range(1,len(points)):
            if points[i][0] > prev[1]: 
                res += 1
                prev = points[i]
            else:
                prev[1] = min(prev[1], points[i][1])

        return res

