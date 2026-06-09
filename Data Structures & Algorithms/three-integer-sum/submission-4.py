class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        idx_lookup = {num:i for i,num in enumerate(nums)}
        all_nums = set([-num for num in nums])
        midpoint = len(nums) // 2

        results = set()
        for i in range(len(nums)-1):
            for j in range(i, len(nums)-1):
                partial_sum = nums[i] + nums[j]
                if partial_sum in all_nums:
                    k = idx_lookup[-partial_sum]
                    if len(set([i,j,k])) == 3:
                        key = [nums[i],nums[j],nums[k]]
                        results.add(tuple(sorted(key)))

        print(results)
        return list(results)

        