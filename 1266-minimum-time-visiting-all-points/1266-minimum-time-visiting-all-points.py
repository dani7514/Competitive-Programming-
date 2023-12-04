class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        seconds=0
        for i in range(len(points)-1):
            temp=points[i]
            temp1=points[i+1]
            if temp[0]==temp1[0]:
                seconds+=abs(temp1[1] - temp[1])
            elif temp[1]==temp1[1]:
                seconds+=abs(temp1[0] - temp[0])
            else:
                t=abs(temp1[0] - temp[0])
                p=abs(temp1[1] - temp[1])
                
                seconds+=max(t,p)
                
        return seconds
               
            