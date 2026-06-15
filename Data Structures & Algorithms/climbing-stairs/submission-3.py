class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [1,2]

        for i in range(n-2):
            old_val = dp[1]
            next_val = dp[1] + dp[0]
            
            dp = [old_val,next_val]

        return dp[-1]
        