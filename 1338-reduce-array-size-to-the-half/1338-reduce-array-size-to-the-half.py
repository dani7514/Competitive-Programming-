class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arr.sort()
        tmpSum=0
        count=0
        dic = Counter(arr)
        dic = dict(sorted(dic.items(), key = lambda item: item[-1], reverse =True))
        for i in dic:
            tmpSum+=dic[i]
            count+=1
            if tmpSum>=len(arr)//2:
                return count
        