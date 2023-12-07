class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        final = [0] *len(boxes)
        sum_balls = 0
        len_balls = 0 
        for i in range(len(boxes)):
            final[i] =  len_balls * i - sum_balls
            if boxes[i] == '1':
                len_balls += 1
                sum_balls += i
                for j in range(i):
                    final[j] += (i-j)
                    
        return final
        