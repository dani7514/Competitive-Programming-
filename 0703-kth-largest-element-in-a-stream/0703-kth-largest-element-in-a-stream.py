class KthLargest:

    def __init__(self, k, nums):
        self.k = k 
        self.heap = nums
        heapify(self.heap)
        while len(self.heap) > k:
            heappop(self.heap)


    def add(self, val):
        heappush(self.heap, val)
        return self.getKthLargest()

    def getKthLargest(self):
        if self.k < len(self.heap):
            heappop(self.heap)

        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)