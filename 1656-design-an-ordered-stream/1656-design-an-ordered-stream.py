class OrderedStream:

    def __init__(self, n: int):
        self. arr = [''] * (n+1)
        self.pointer = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.arr[idKey] = value
        
        while self.pointer < len(self.arr) and self.arr[self.pointer] != '':
            self.pointer += 1
            
        
        return self.arr[idKey:self.pointer]
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)