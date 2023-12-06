class Solution:
    def totalMoney(self, n: int) -> int:
        total_money = 1
        monday = 1
        temp = 1
        for i in range(1,n):
            if i % 7 == 0 :
                monday += 1
                total_money += monday 
                temp = monday 
            else:
                temp += 1
                total_money += temp
                
              
                
        return  total_money
                
                
                

        