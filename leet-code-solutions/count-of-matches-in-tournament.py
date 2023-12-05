class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        
        #iterate to get the number of matches played in the tournament until a winner is decided.
        while n > 1:
            if n % 2 == 0:
                matches += n / 2
                n = n / 2
            else:
                matches += (n - 1) / 2
                n = (n - 1) / 2 + 1
                
        return int(matches)
        