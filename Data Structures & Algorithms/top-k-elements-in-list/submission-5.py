class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        

        heap = []
        heapq.heapify(heap)
        for num, num_count in freq.items():
            heapq.heappush(heap, (num_count, num))
            if len(heap) > k:
                heapq.heappop(heap)

        result = [num for (num_count,num) in heap]

        return result