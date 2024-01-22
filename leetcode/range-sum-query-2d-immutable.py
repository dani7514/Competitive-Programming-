class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = []

        for _ in range(len(matrix)):
            self.prefix.append([0] * len(matrix[0]))

        for row in range(len(matrix)):
            prefix = 0
            for col in range(len(matrix[0])):
                prefix += matrix[row][col]
                self.prefix[row][col] = prefix
                if row >= 1:
                    self.prefix[row][col] += self.prefix[row-1][col]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum_region = self.prefix[row2][col2]
        if row1 > 0:
            sum_region -= self.prefix[row1-1][col2]
            if col1 > 0:
                sum_region += self.prefix[row1-1][col1-1]

        if col1 > 0:
            sum_region -= self.prefix[row2][col1-1]

        return sum_region


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)