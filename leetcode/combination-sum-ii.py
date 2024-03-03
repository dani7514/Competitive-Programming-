class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(start,curr,total):
            if total == target:
                res.append(curr[:])
                return
            
            if start>=len(candidates) or total > target:
                return

            for i in range(start,len(candidates)):
                if candidates[i]>target-total or (i>start and candidates[i]==candidates[i-1]):
                    continue
                curr.append(candidates[i])
                total+=candidates[i]
                backtrack(i+1,curr,total)
                curr.pop()
                total-=candidates[i]
        backtrack(0,[],0)
        return res