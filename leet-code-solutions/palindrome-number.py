class Solution:
    def isPalindrome(self, x: int) -> bool:
        string=str(x)
        i=0
        j=len(string)-1
        while i<=j:
            if string[i]==string[j]:
                i+=1
                j-=1
            else:
                return False
        return True