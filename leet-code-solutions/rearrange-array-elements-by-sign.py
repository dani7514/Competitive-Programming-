class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        arr1=[]
        arr2=[]
        
        for i in nums:
            if abs(i)==i:
                arr1.append(i)
            else:
                arr2.append(i)
        
        j=0
        result=[]
        for k in arr1:
            result.append(k)
            result.append(arr2[j])
            j+=1
            
        return result