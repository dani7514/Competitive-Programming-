class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i=0
        j=round(c**(1/2))
        while i<=j:
            if i**2 + j**2 > c:
                j-=1
            elif i**2 + j**2 < c:
                i+=1
            else:
                return True
        else: 
            return False