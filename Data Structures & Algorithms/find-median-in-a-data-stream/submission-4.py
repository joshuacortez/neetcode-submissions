import heapq
class MedianFinder:
    # Main idea: the median is what's in between the minheap and the maxheap
    def __init__(self):
        # maxheap is for the smaller values
        # python 3.14 has max heap
        self.maxheap = []
        heapq.heapify_max(self.maxheap)

        # minheap is for the larger values
        self.minheap = []
        heapq.heapify(self.minheap)

    def addNum(self, num: int) -> None:
        # by default, add the number to the maxheap
        heapq.heappush_max(self.maxheap, num)
        
        # if the maxheap value is greater than or equal the minheap value, pop from the maxheap and push to the minheap  
        if self.minheap and self.maxheap[0] >= self.minheap[0]:
            maxheap_val = heapq.heappop_max(self.maxheap)
            heapq.heappush(self.minheap, maxheap_val)
        
        # if the minheap value is less than or equal the maxheap value, pop from the minheap and push to the maxheap
        while self.minheap and self.minheap[0] >= self.maxheap[0]:
            minheap_val = heapq.heappop(self.minheap)
            heapq.heappush_max(self.maxheap, minheap_val)

        # if the length of the two heaps differ by more than 1, pop from the maxheap and push to the minheap
        while len(self.maxheap) > len(self.minheap) + 1:
            val = heapq.heappop_max(self.maxheap)
            heapq.heappush(self.minheap, val)

    def findMedian(self) -> float:
        if self.minheap:
            median_minheap = self.minheap[0]
        if self.maxheap:
            median_maxheap = self.maxheap[0]

        # if one heap is longer than the other, we return the val of that
        if len(self.minheap) > len(self.maxheap):
            median = median_minheap
        elif len(self.minheap) < len(self.maxheap):
            median = median_maxheap
        # if the length of both of the heaps is the same, we return the average
        else:
            median = (median_minheap + median_maxheap)/2

        return median
        