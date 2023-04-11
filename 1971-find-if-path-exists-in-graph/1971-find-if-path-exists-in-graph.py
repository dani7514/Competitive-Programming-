class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph=defaultdict(list)
       
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
            
        visited=set()
        visited.add(source)
        queue=deque([source])
        
        while queue:
            node=queue.popleft()    
            if node==destination:
                return True
            
            for i in graph[node]:
                if not i in visited:
                    queue.append(i)
                    visited.add(i)
        return False
        
        