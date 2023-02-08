class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        record = []
        for trip in trips:
            record.append([trip[1], trip[0]])
            record.append([trip[2], -trip[0]])

        record.sort() 
        
        num_passengers = 0
        for r in record:
            num_passengers += r[1]
            if num_passengers > capacity:
                return False
        return True
        