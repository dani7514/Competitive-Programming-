class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque([i for i in range(len(tickets))])
        
        time = 0
        while q:
            for i in range(len(q)):
                
                node = q.popleft()
                tickets[node] -= 1

                if tickets[node] >= 1:
                    q.append(node)
                
                time += 1
                if tickets[k] == 0:
                    return time
                
