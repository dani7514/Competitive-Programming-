class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        reveal=[i for i in range(len(deck))]
        unreveal=reveal.copy()
        
        deck.sort()
        
        for j in range(len(deck)):
            reveal[unreveal.pop(0)]=deck[j]
            if unreveal:
                unreveal.append(unreveal.pop(0))
        return reveal
            
            