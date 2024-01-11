class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = len(blocks)
        for i in range(len(blocks)):
            select = blocks[i:i+k]
            if len(select) == k:
                if select.count('W') < res:
                    res = select.count('W')
            else:
                break
        return res
        