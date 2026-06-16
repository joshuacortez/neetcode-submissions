class Solution:
    def rob(self, nums: List[int]) -> int:
        # Decision 1: are you gonna rob the first house or not?
        # Decision 2: are you gonna skip each house i or not?
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        def rob_linear(nums: List[int]) -> int:
            n = len(nums)
            if n <= 2:
                return max(nums)
                
            dp = [nums[0], max(nums[:2])]
            for i in range(2,len(nums)):
                rob_i = nums[i] + dp[0]
                skip_i = dp[1]
                best_i = max(rob_i, skip_i)

                new_dp = [dp[1], best_i]
                dp = new_dp
            
            return dp[-1]
        
        n = len(nums)
        rob_first = rob_linear(nums[:n-1])
        rob_last = rob_linear(nums[1:])
        best = max(rob_first, rob_last)
        return best