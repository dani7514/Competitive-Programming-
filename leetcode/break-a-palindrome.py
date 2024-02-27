class Solution:
    def breakPalindrome(self, palindrome: str) -> str:

        if len(palindrome) == 1:
            return ""

        temp = "a" * len(palindrome)
        if temp == palindrome:
            return ("a" * (len(palindrome)-1)) + "b"

        t = ''
        res = ''
        for i in range(len(palindrome)):
            if palindrome[i] != "a":
                t += palindrome[:i] + "a" + palindrome[i+1:]

                if t == temp:
                    continue
                else:
                    res = t
                break

        if res == "":
            return palindrome[:len(palindrome)-1] + "b"
            
        return res


