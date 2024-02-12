class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:

        for i in matrix:
            for j in range(len(i)-1):
                i[j+1]+=i[j]

        count = 0
        for k in range(len(matrix)):
            for l in range(k,-1,-1):
                if k == l:
                    s = matrix[k][:]
                else:
                    s = [s[i]+matrix[l][i] for i in range(len(matrix[0]))]
                r = {0:1}
                for u in s:
                    if u-target in r:
                        count += r[u-target]
                    r[u] = r.get(u,0)+1
        return count