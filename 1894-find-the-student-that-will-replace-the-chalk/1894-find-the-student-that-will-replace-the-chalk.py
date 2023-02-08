class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s=sum(chalk)
        ans=k%s
            
        n=len(chalk)
        for i in range(n):
            ans-=chalk[i]
            if (ans<0):
                return i
        