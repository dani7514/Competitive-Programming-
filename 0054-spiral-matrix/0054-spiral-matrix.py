class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        visited = set()
        direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        ans = []

        def inbound(x, y):
            return 0 <= x < n and 0 <= y < m

        def gr(x, y, d):
            visited.add((x, y))
            ans.append(matrix[y][x])

            for _ in range(4):
                nx, ny = x + direction[d][0], y + direction[d][1]
                if inbound(nx, ny) and (nx, ny) not in visited:
                    gr(nx, ny, d)
                d = (d + 1) % 4  

        gr(0, 0, 0)  
        return ans

        
        