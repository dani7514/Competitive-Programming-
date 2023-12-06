class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        container_hashtable = {}
        
        for index in range(len(nums)) :
            temporary = target - nums[index]
            
            if temporary in  container_hashtable :
                return [index, container_hashtable[temporary]]
            else:
                container_hashtable[nums[index]] = index
                        
        return []
                
            