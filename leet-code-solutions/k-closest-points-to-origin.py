class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_container = []
     
        for i in points:
            y = (i[0]**2 + i[1]**2)**0.5
            y = [i,y]
            distance_container.append(y)
        
        distance_container.sort(key = lambda x:x[1])
        x = distance_container[0][1]
        j = 0
        result = []

        while j < k:
            result.append(distance_container[j][0])
            j+=1
        return result