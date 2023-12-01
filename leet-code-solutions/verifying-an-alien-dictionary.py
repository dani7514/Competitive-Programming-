class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        tempDic={}
        c=1
        for i in order:
            tempDic[i]=c
            c+=1     
        j=0
        k=1
        while k < len(words):
            for p in range(len(words[j])):
                if p <len(words[j]) and p >= len(words[k]):
                    return False
                if tempDic[words[j][p]] > tempDic[words[k][p]]:
                    return False
                elif tempDic[words[j][p]] < tempDic[words[k][p]]:
                    break
                else:
                    continue      
            j+=1
            k+=1
        return True
        