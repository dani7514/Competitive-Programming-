class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = ["0"]
        for digi in num:
            while k and stack[-1]>digi:
                stack.pop()
                k -= 1
            stack.append(digi)
        while k:
            stack.pop()
            k -= 1
        return max("0", "".join(stack).lstrip("0"))
        