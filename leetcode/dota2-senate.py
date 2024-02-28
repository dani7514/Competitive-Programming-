class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        if len(senate) == 1:
            if senate[0] == "R":
                return "Radiant"
            else:
                return "Dire"

        R_queue = []
        D_queue = []
        count = 0

        for i in range(len(senate)):
            if senate[i] == "R":
                R_queue.append(i)
            else:
                D_queue.append(i)
        
        for _ in range(len(senate)):
            if R_queue and not D_queue:
                return "Radiant"

            if not R_queue and D_queue:
                return "Dire"

            if R_queue[0] < D_queue[0]:
                D_queue.pop(0)
                R_queue.append(R_queue.pop(0) + len(senate))

            else:
                R_queue.pop(0)
                D_queue.append(D_queue.pop(0) + len(senate))


