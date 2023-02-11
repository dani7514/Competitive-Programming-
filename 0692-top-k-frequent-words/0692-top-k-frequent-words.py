class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        maxwordlen=0
        mp={}
        for word in words:
            maxwordlen=max(maxwordlen,len(word))
            mp[word]=mp.get(word,0)+1
        q=[]
        for key in mp:
            cmpstr=""
            for i in range(maxwordlen):
                x=ord(key[i]) if i<len(key) else ord("a")-1
                cmpstr+=chr(ord("z")-x+ord("a"))
            if len(q)<k:
                heapq.heappush(q,(mp[key],cmpstr,key))
            elif mp[key]>q[0][0] or (mp[key]==q[0][0] and cmpstr>q[0][1]):
                heapq.heappop(q)
                heapq.heappush(q,(mp[key],cmpstr,key))
        res=[]
        for i in range(k):
            res.append(heapq.heappop(q)[2])
        return res[::-1]
        