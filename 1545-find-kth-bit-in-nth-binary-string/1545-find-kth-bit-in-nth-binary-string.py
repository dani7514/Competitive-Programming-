class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        p=self.recursion(n,k)
        return p[k-1]
      
    def recursion(self, n: int, k: int) -> str:
        if n==1:
            return "0"
        else:
            p=str(self.recursion(n-1,k)) + "1" + self.reverse(self.invert(str(self.recursion(n-1,k))))
            return p
    def reverse(self, inverse_s: str) -> str:
        return inverse_s[::-1]
    def invert(self, tmp: str) -> str:
        inverse_s = tmp.replace('1', '2')
        inverse_s = inverse_s.replace('0', '1')
        inverse_s = inverse_s.replace('2', '0')
        return inverse_s
        
            

            