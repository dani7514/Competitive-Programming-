class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        store_diagonals = {}

        for i in range(len(mat)):
            temp_arr = []
            for j in range(len(mat[i])):
                temp_sum = i + j
                if temp_sum in store_diagonals:
                    store_diagonals[temp_sum].append(mat[i][j])
                else:
                    store_diagonals[temp_sum] = [mat[i][j]]
        
        result = []

        for i in store_diagonals:
            if i % 2 == 0:
                store_diagonals[i].reverse()
                result += store_diagonals[i]
            else:
                result += store_diagonals[i]
        
        return result