class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        start = 0
        shuffle_index = n
        shuffled_arr = []
        
        while start < n:
            shuffled_arr.append(nums[start])
            shuffled_arr.append(nums[shuffle_index])
            shuffle_index += 1
            start += 1
            
        return  shuffled_arr
                
            
        