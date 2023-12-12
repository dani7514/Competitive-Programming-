class UndergroundSystem:

    def __init__(self):
        self.check_in = {}
        self.total_distance = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        get_startStation = self.check_in[id][0]
        get_startTime = self.check_in[id][1]
        
        start_end = (get_startStation, stationName)
        total =  t - get_startTime
        
        if start_end in self.total_distance:
            self.total_distance[start_end].append(total)
        else:
            self.total_distance[start_end] = [total] 
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        set_station = (startStation, endStation)
        get_the_array = self.total_distance[set_station]
        
        get_avarage = sum(get_the_array)/len(get_the_array)
        
        return get_avarage
        
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)