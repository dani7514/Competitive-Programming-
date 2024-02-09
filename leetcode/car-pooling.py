class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pickup_dropoff = []

        for i in trips:
            pickup_dropoff.append([i[1],i[0]])
            pickup_dropoff.append([i[2],-i[0]])

        pickup_dropoff.sort()
       
        num_passenger = 0

        for i in pickup_dropoff:
            num_passenger += i[1]

            if num_passenger > capacity:
                return False
        
        return True
