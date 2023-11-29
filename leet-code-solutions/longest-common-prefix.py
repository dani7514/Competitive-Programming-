class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minL=float('inf')
        for i in strs:
            if len(i)<minL:
                minL=len(i)

        st=''
        t=False
        for j in range(minL):
            tmp=strs[0][j]
            print(tmp)
            for k in range(1,len(strs)):
                if strs[k][j] != tmp:
                    t=True
            if t==True:
                break
            st+=tmp
        return st