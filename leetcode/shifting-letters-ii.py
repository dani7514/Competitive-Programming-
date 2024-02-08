class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        chars = "abcdefghijklmnopqrstuvwxyz"
        index_to_char = {}

        for i, c in enumerate(chars):
            index_to_char[i] = c

        chars = [ord(c) - ord("a") for c in s]
        prefix = [0] * len(s)
        
        for start, end, direction in shifts:
            prefix[start] += 1 if direction == 1 else -1
            if end + 1 < len(prefix):
                prefix[end + 1] -= 1 if direction == 1 else -1

        for i in range(1, len(prefix)):
            prefix[i] += prefix[i-1]

        for i in range(len(chars)):
            chars[i] = (chars[i] + prefix[i]) % 26

        chars = [index_to_char[c] for c in chars]
        return "".join(chars)