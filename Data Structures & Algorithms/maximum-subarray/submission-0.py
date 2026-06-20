class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cum_sum = 0
        max_sum = float("-inf")

        for num in nums:
            cum_sum = max(cum_sum, 0)
            cum_sum += num

            max_sum = max(cum_sum, max_sum)
        
        return max_sum