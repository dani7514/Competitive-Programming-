class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        m = len(mat)
        left = [0,0]
        right = [0,m-1]
        count = 0
        if m == 1:
            return mat[0][0]
        while left[0] <= m-1:
            count += mat[left[0]][left[1]]
            left[0]+=1
            left[1]+=1
            count += mat[right[0]][right[1]]
            right[0]+=1
            right[1]-=1
        if m % 2 == 1:
            mid = (m-1)//2
            count -= mat[mid][mid]
        return count