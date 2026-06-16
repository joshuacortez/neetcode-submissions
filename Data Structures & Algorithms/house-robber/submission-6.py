class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        cache = {1:nums[0], 2:max(nums[:2])}

        def dfs(nums, i, cache):
            curr = nums[:i]
            
            if i <= 2:
                return max(curr)

            if i in cache:
                return cache[i]

            # scenario 1: rob house i, that means you skip i-1
            # and get best result as of i-2
            scen_1 = curr[-1] + dfs(nums, i-2, cache)

            # scenario 2: skip house i, that means you get best result as of i-1
            scen_2 = dfs(nums, i-1, cache)

            cache[i] = max(scen_1,scen_2)
            return cache[i]
        
        dfs(nums, n, cache)

        return cache[n]