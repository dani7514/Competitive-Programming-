class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        sumT=0
        for i in range(1,len(salary)-1):
            sumT+=salary[i]
        return sumT/(len(salary)-2)
            
            