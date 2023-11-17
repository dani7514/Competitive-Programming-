class Solution:
    def originalDigits(self, s: str) -> str:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        
        num = [0] * 10
        
        num[0] = count[ord('z') - ord('a')]
        num[2] = count[ord('w') - ord('a')]
        num[4] = count[ord('u') - ord('a')]
        num[6] = count[ord('x') - ord('a')]
        num[8] = count[ord('g') - ord('a')]
        
        num[1] = count[ord('o') - ord('a')] - num[0] - num[2] - num[4]
        num[3] = count[ord('h') - ord('a')] - num[8]
        num[5] = count[ord('f') - ord('a')] - num[4]
        num[7] = count[ord('s') - ord('a')] - num[6]
        num[9] = count[ord('i') - ord('a')] - num[5] - num[6] - num[8]
        
        result = ''.join(str(i) * num[i] for i in range(10))
        return result
        