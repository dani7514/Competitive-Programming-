class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        def pow(x, n):

            if n == 0: 
                return 1

            if n == 1: 
                return x

            if n % 2 == 0: 
                ans = pow(x, n / 2)
                return (ans * ans) % MOD
            else:
                ans = pow(x, (n - 1) / 2)
                return (x * ans * ans) % MOD

        even = n // 2
        odd = n - even

        res = ((pow(4, even) % MOD * pow(5, odd) % MOD) % MOD)
        
        return res