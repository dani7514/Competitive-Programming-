class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = []
        for i in range(1,n+1):
            nums.append(i)

        def backtrack(i,path):
            if len(path) == k:
                ans.append(path[:])
                return

            if i >= n:
                return
           
            path.append(nums[i])
            backtrack(i+1,path)
            path.pop()

            backtrack(i+1,path)

        ans = []
        backtrack(0,[])

        return ans



