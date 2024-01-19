class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        arr=[]
        temp=0
        
        for i in nums:
            arr.append(temp+i)
            temp+=i
        for j in range(len(arr)):
            if j==0:
                if arr[len(arr)-1]-arr[j]==0:
                    return j
            elif j==len(arr)-1:
                if arr[j-1]==0:
                    return j
            else:
                if arr[len(arr)-1]-arr[j]==arr[j-1]:
                    return j
        return -1   
        
        