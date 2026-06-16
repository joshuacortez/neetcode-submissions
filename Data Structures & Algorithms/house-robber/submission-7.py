class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        dp = [nums[0], max(nums[:2])]

        for i in range(2,len(nums)):
            skip_i = dp[-1]
            rob_i = dp[0] + nums[i]
            best_i = max(skip_i, rob_i)

            new_dp = [dp[-1], best_i]
            dp = new_dp
        
        return dp[-1]