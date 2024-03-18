class Solution:
    def totalNQueens(self, n: int) -> int:
        col, l2r, r2l = set(), set(), set()
        res = 0

        def check(r, c):
            if c in col or r + c in r2l or c - r in l2r:
                return False
            return True
        
        def dfs(x):
            nonlocal res
            if x == n:
                res += 1
                return
            
            for i in range(n):
                if check(x, i):
                    col.add(i)
                    l2r.add(i - x)
                    r2l.add(x + i)
                    
                    dfs(x + 1)
                    
                    col.remove(i)
                    l2r.remove(i - x)
                    r2l.remove(i + x)
        
        dfs(0)
        return res