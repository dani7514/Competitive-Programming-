class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xorSum=0
        answer=[]
        for i in range(len(arr)):
            xorSum^=arr[i]
            arr[i]=xorSum
        for l,r in queries:
            if l==0:
                answer.append(arr[r])
            else:
                answer.append(arr[r]^arr[l-1])
        return answer
        