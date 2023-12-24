class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        max_number_index = arr.index(max(arr))

        if max_number_index == 0 or max_number_index == len(arr)-1:
            return False

        for i in range(max_number_index):
            if arr[i] >= arr[i+1]:
                return False

        for i in range(max_number_index,len(arr)-1):
            if arr[i] <= arr[i+1]:
                return False
                
        return True