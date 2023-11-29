class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        arr=[]
        temp=num//3
        if ((temp + (temp +1) + (temp-1))==num):
            arr.append(temp-1)
            arr.append(temp)
            arr.append(temp+1)
            return arr
        else:
            return []
        
            
            
        
        
        
        