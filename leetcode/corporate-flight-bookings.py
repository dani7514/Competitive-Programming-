class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        arr = [0]*(n+1)
        for start, end, seats in bookings:
            arr[start-1]+= seats
            arr[end]-= seats
           
        return list(accumulate(arr[:-1]))


        

        