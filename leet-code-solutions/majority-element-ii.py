class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        container_dict = {}
        
        for element in nums:
            if element in container_dict:
                container_dict[element] += 1
            else:
                container_dict[element] = 1
         
        result = []
        for element_in_dict in container_dict:
            if container_dict[element_in_dict] > len(nums)/3:
                result.append(element_in_dict)
        
        return result
                
        