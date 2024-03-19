class TimeMap:

    def __init__(self):
        self.x = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.x:
            self.x[key] = []
            for _ in range(timestamp-1):
                 self.x[key].append("")
        if len(self.x[key]) < timestamp-1:
            last = self.x[key][-1]
            for _ in range(timestamp-len(self.x[key])-1):
                self.x[key].append(last)
        self.x[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.x:
            return ""
        if len(self.x[key]) < timestamp:
            return self.x[key][-1]
        return self.x[key][timestamp-1]

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)