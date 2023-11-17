class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        con={}
        arr=[]
        for i in nums:
            if i in con:
                con[i]+=1
            else:
                con[i]=1
        
        sortedCon=dict(sorted(con.items(), key=lambda x:x[1], reverse=True))
        
        getItem=list(sortedCon.items())
        print(getItem)
        
        for j in range(k):
            arr.append(getItem[j][0])
        return arr
                
            
        