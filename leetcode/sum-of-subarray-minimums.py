class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        results = []
        stack = []
        for i, num in enumerate(arr):
            while stack and num < arr[stack[-1]]:
                stack.pop()
            
            if stack:
                result = results[stack[-1]] + (i-stack[-1])*num
                results.append(result)
            else:
                results.append((i+1)*num)

            stack.append(i)
        return sum(results) % (10**9+7)


