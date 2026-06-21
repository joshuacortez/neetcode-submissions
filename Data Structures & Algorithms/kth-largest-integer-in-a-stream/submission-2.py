import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapq.heapify(nums)
        self.nums = nums
        
    def add(self, val: int) -> int:
        
        # if the size of the heap is more than k
        # kth largest also means n-k+1th smallest
        # e.g. if n = 5, k = 2, 2nd largest is 5-2+1 or 4th smallest

        # we add the current value
        heapq.heappush(self.nums, val)

        # we pop until we have k remaining, so we popped n-k+1 elements
        # we start with n + 1 because we added
        # then we popped (n-k+1) because (n+1) - (n-k+1) = k 
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

        # the last element should be the n-k+1th element
        return self.nums[0]