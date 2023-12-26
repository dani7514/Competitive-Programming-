class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        grid = defaultdict(set)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] != '.':
                    num = board[row][col]
                    if num in rows[row]:
                        return False
                    if num in cols[col]:
                        return False
                    if num in grid[(row // 3, col // 3)]:
                        return False
                    rows[row].add(num)
                    cols[col].add(num)
                    grid[(row // 3, col // 3)].add(num)

        return True