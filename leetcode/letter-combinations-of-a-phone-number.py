class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        dic={'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
        res=[]
        n=len(digits)
        def backtracking(r):
            if len(r)==n:
                res.append(r)
            else:
                for i in dic[digits[len(r)]]:
                    backtracking(r+i)
        backtracking("")            
        return res