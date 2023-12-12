class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.expired_time = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.expired_time[tokenId] = self.timeToLive + currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        get_expiryTime = 1
        if tokenId in self.expired_time:
            get_expiryTime =  self.expired_time[tokenId]
        
            if currentTime < get_expiryTime:
                self.expired_time[tokenId] = self.timeToLive + currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for token in self.expired_time:
            if  self.expired_time[token] > currentTime:
                count += 1
            
        return count
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)