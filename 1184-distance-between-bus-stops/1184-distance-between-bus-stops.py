class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        a= min(start, destination)
        b = max(start, destination)
        sumC=sum(distance[a:b])
        sumU=sum(distance) - sumC
        minT= min(sumU, sumC)
        
        return minT
       