class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def solve(cand, t, pre, arr):
            if pre == t:
                res.append(sorted(arr.copy()))
            
            if pre > t:
                return
            
            for i in cand:
                arr.append(i)
                solve(cand, t, pre + i, arr)
                arr.pop()
        
        solve(candidates, target, 0, [])
        
        n = len(res)
        ans = []
        for i in range(n):
            if res[i] in ans:
                continue
            ans.append(res[i])
        return ans