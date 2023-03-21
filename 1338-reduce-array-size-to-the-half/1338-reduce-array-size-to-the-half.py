class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arr.sort()
        dic={}
        tmpArr=[]
        tmpSum=0
        count=0
        for i in arr:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for j in dic:
            tmpArr.append(dic[j])
        tmpArr.sort()
        for i in range(len(tmpArr)-1,-1,-1):
            tmpSum+=tmpArr[i]
            count+=1
            if tmpSum>=len(arr)//2:
                return count
        