class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        smooth=0
        count=0
        nums=0

        for i in range(0,len(prices)):
            if i==0:
                count+=1
                count+=count-1
                nums+=1
            else:
                if prices[i]-prices[i-1]==-1:
                    nums+=1
                    count+=nums-1
                    count+=1

                else:
                    smooth+=count
                    count=1
                    nums=1

        smooth+=count

        return smooth 
        