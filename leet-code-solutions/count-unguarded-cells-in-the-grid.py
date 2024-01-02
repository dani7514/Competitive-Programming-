class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        set_guards = set((r, c) for r, c in guards)
        set_walls = set((r, c) for r, c in walls)
        set_cells = set((r, c) for r in range(m) for c in range(n))
        set_cells -= set_guards
        set_cells -= set_walls
        seen_cells = set()

        for guard_row, guard_col in set_guards:
            
            r, c = guard_row, guard_col + 1
            while (r, c) in set_cells:
                seen_cells.add((r, c))
                c += 1
            
            r, c = guard_row, guard_col - 1
            while (r, c) in set_cells:
                seen_cells.add((r, c))
                c -= 1
            
            r, c = guard_row + 1, guard_col
            while (r, c) in set_cells:
                seen_cells.add((r, c))
                r += 1
            
            r, c = guard_row - 1, guard_col
            while (r, c) in set_cells:
                seen_cells.add((r, c))
                r -= 1

        return len(set_cells - seen_cells)