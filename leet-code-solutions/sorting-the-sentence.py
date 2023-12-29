class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split()
        arr.sort(key= lambda x:x[-1])
        temp = []
        
        for i in arr:
            temp.append(i[:-1])

        return " ".join(temp)