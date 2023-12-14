class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        good_meal_dict = {}
        mod = 10**9 + 7
        count = 0
        
        for meal in deliciousness:
            if meal in good_meal_dict:
                good_meal_dict[meal] += 1
            else:
                good_meal_dict[meal] = 1
                
        for meal in deliciousness :
            good_meal_dict[meal] -= 1
            for i in range(22):
                temp = 2**i - meal
                if temp in good_meal_dict :
                    count += good_meal_dict[temp]
                
        return count % mod
            
        
        