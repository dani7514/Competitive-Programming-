class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        l=[]
        for i in range(n):
            l.append(str(nums[i]))

        for i in range(0,n):
            for j in range(i,n):
                m = l[i]+''+l[j]
                k = l[j]+''+l[i]
                if(int(k)>int(m)):
                    t=l[i]
                    l[i]=l[j]
                    l[j]=t

        h=0
        for i in range(n):
            if(nums[i]==0):
                h=h+1
                if(h==n):
                    return '0'

        c=''.join(l)
        return c
        