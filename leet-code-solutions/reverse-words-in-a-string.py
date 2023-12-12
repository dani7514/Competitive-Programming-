class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(" ")
        arr = arr[::-1]
        result = ''
        
        for index in range(len(arr)):
            if arr[index] != "":
                result += arr[index] + " "
                
        return result.strip()
    
       
        