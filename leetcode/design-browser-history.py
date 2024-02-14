class Node:
    def __init__(self, value, nextN = None, prev = None):
        self.value = value
        self.prev = prev
        self.next = nextN


class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = Node(homepage)


    def visit(self, url: str) -> None:

        visited = Node(url)
        self.history.next = visited
        visited.prev = self.history

        self.history = visited

    def back(self, steps: int) -> str:

        while self.history.prev and steps:
             self.history = self.history.prev
             steps -= 1

        return self.history.value
        
    def forward(self, steps: int) -> str:

        while self.history.next and steps: 
            self.history = self.history.next; 
            steps -= 1

        return self.history.value
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)