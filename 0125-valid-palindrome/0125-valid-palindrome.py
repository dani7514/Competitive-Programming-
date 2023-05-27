class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        letters='abcdefghijklmnopqrstuvwxyz'
        cap='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        num='0123456789'
        temp=''
        for i in s:
            if i in letters or i in cap or i in num:
                if i in cap:
                    t=ord(i)+32
                    temp+=chr(t)
                else:
                    temp+=i
        reverse=temp[::-1]
        if reverse==temp:
                return True
        return False
        
        