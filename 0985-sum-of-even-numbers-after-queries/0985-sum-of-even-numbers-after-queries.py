class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum_container = []
        even_dict = set()
        even_sum = 0
        
        
        for number in range(len(nums)):
            if nums[number] % 2 == 0:
                even_sum += nums[number]
                even_dict.add(number)
            
        
        
        for query in queries:
            temp = nums[query[1]] + query[0]
            if temp % 2 == 0:
                if query[1] in even_dict:
                    even_sum -= nums[query[1]]
                    even_sum += temp
                    even_sum_container.append(even_sum)
                else:
                    even_sum += temp
                    even_dict.add(query[1])
                    even_sum_container.append(even_sum)
            else:
                if query[1] in even_dict:
                    even_sum -= nums[query[1]]
                    even_dict.remove(query[1])
                    even_sum_container.append(even_sum)
                else:
                    even_sum_container.append(even_sum)
                    
            nums[query[1]] = temp
        if not even_sum_container:
            return [0]
        return even_sum_container
            
                
        
            