class Solution:
    def replaceDigits(self, s: str) -> str:
        i=0
        new=''
        while i<len(s):
            if i+1 < len(s) :
                temp=chr(ord(s[i])+int(s[i+1]))
                new=new+s[i]+ temp
            else:
                new+=s[i]
            i+=2
        return new
            
