class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0

        for i in range(len(strs[0])):
            temp_str = strs[0][i]
            flag = True
            for j in range(1,len(strs)):
                if temp_str <= strs[j][i]:
                    temp_str = strs[j][i]
                else:
                    flag = False
                    break
            if not flag:
                count += 1

        return count