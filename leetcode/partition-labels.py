class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}

        for i in range(len(s)):
            last[s[i]] = i

        last_pos = 0
        result = []
        start = 0

        for i in range(len(s)):
            last_pos = max(last_pos,last[s[i]])

            if i == last_pos:
                result.append(last_pos - start + 1)
                start = i + 1

        return result