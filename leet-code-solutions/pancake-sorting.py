class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        output=[]
        tail=len(arr)
        while tail!=1:
            t=arr.index(tail)
            if t!=tail-1:
                output+=[t+1,tail]
                
                arr=arr[t::-1]+arr[t+1:]
                
                arr=arr[tail-1::-1]+arr[tail:]
                
            tail-=1
        return output
        