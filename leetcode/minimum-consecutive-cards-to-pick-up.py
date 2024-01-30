class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        left = 0
        res = float('inf')
        last_index_container = {}

        for right in range(len(cards)):

            if cards[right] not in last_index_container:
                last_index_container[cards[right]] = 1
            else:
                last_index_container[cards[right]] += 1

            if last_index_container[cards[right]] == 2:

                while cards[left] != cards[right]:
                    last_index_container[cards[left]] -= 1
                    left += 1

                res = min(res, right-left+1)

                last_index_container[cards[right]] -= 1
                left += 1

        if res != float('inf'):
            return res
        return -1 

    