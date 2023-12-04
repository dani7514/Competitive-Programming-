class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        arr=[]
        for i in range(len(candies)):
            temp=candies[i]+extraCandies
            if temp >= max(candies):
                arr.append(True)
            else:
                arr.append(False)
        return arr
                
        