class Solution(object):
    def sortSentence(self, s):
        word=s.split()
        for i in range(1,len(word)+1):
            for j in word:
                index=len(j)-1
                if i ==int(j[index]):
                    for k in range(len(word)):
                        if word[k]==j:
                            word[i-1],word[k] = word[k] ,word[i-1]
        s=""
        for i in word:
            m=""
            for j in range(len(i)-1):
                m+=i[j]
            s=s+m
            for k in range(len(word)):
                if word[k]==i:
                    if k!=len(word)-1:
                        s+=" "
        return s

        