import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            heaviest = heapq.heappop_max(stones)
            if not stones:
                return heaviest
            second_heaviest = heapq.heappop_max(stones)

            if heaviest > second_heaviest:
                new_stone = heaviest - second_heaviest
                heapq.heappush_max(stones, new_stone)

        if stones:
            return stones[0]
        else:
            return 0