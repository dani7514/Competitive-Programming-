class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        firstIndex=0
        new=''
        for k in shifts:
            firstIndex+=(k%26)
            
        sumArr=[firstIndex%26]
        for i in range(1,len(shifts)):
            firstIndex=(firstIndex)-(shifts[i-1]%26)
            sumArr.append(firstIndex%26)
            
        for i in range(len(s)):
            n=ord(s[i])+sumArr[i]
            if n>ord("z"):
                n-=26
            new+=chr(n)
        return new
            
        