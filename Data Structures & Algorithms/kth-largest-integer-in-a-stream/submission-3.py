import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapq.heapify(nums)
        self.nums = nums

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        # kth largest means it's n-k+1th smallest
        # e.g. if n = 5, 2nd largest is (5-2+1) or 4th smallest

        nth_smallest = len(self.nums) - self.k + 1
        for i in range(nth_smallest-1):
            heapq.heappop(self.nums)

        return self.nums[0]
