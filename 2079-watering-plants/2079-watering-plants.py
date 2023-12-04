class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        water=0
        t=capacity
        i=0
        while i<len(plants):
            if plants[i] <= t:
                water+=1
            else:
                water+=2*(i) + 1
                t=capacity
              
            t-=plants[i]
            i+=1
            
            
        return water 
                
                
                
                
            