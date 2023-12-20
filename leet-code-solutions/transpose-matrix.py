class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = []
        for i in range(len(matrix[0])):
            temp_arr = []
            temp_arr.append(matrix[0][i])

            for j in range(1,len(matrix)):
                temp_arr.append(matrix[j][i])
            
            result.append(temp_arr)

        return result 