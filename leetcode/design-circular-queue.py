class MyCircularQueue:
    
    def __init__(self, k: int):
        self.maxSize = k
        self.queue = []

    def enQueue(self, value: int) -> bool:
        if len(self.queue) == self.maxSize:
            return False
        self.queue.append(value)
        return True
        
    def deQueue(self) -> bool:
        if len(self.queue) == 0:
            return False
        self.queue.pop(0)
        return True
        

    def Front(self) -> int:
         
        if len(self.queue)==0:
            return -1
        else:
            return self.queue[0]

    def Rear(self) -> int:
        if len(self.queue)==0:
            return -1 
        return self.queue[len(self.queue)-1]

    def isEmpty(self) -> bool: 
         if len(self.queue)==0:
            return 1 
         else:
            0

    def isFull(self) -> bool:
        
        if len(self.queue)==self.maxSize:
            return 1 
        else:
            0
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()