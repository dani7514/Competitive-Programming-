class Solution:
    def maxScore(self, s: str) -> int:
        num_one = 0
        for i in s:
            if i == "1":
                num_one += 1

        sum_container = []
        num_zero = 0
        for i in range(len(s)-1):
            if s[i] == "0":
                num_zero += 1
            else:
                num_one -= 1
            
            sum_container.append(num_zero + num_one)

        return max(sum_container)


