class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = 0
        dic = {}
        
        for i in range(len(answers)):
            if answers[i] in dic :
                
                dic[answers[i]] -= 1

                if dic[answers[i]] == 0:
                    dic.pop(answers[i])
                
            else:
                if answers[i] == 0:
                    count += 1
                else:

                    dic[answers[i]] = answers[i]
                    count += (1 + answers[i])
        
        return count 

