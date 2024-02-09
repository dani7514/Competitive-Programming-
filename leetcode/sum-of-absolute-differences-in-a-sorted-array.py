class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        arr=[]
        temp=0
        res=[]
        for i in nums:
            arr.append(temp+i)
            temp+=i
        
        for j in range(len(arr)):
            t=(arr[len(arr)-1]-arr[j])-(nums[j]*(len(arr)-j-1))
            p=(nums[j]*(j+1))-arr[j]
         
            res.append(t+p)
        return res
            
        
                                        
            