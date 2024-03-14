class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        res = []
        
        def backtrack(board, row):
            if n == row:
                res.append([''.join(board[i]) for i in range(n)])
                return 
            
            for col in range(n):
                if not isValid(board, row, col):
                    continue
                
                board[row][col] = 'Q'
                backtrack(board, row+1)
                board[row][col] = '.'
        
        def isValid(board, row, col):
            
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            
            i = row - 1
            j = col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            
            i = row - 1
            j = col + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            
            return True
        
        backtrack(board, 0)
        return res