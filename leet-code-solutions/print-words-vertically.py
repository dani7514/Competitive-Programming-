class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        n = 0
        i = 0
        while i < len(s):
            if len(s[i]) > n:
                n = len(s[i])
            i+=1
        ans = [""]*n
        k = 0
        print(n)
        while k < n:
            for j in range(len(s)):
                if k + 1 <= len(s[j]):
                    ans[k] += s[j][k]
                else:
                    ans[k]+=" "
            k+=1
            modified_list = [a.rstrip() for a in ans]
        return modified_list