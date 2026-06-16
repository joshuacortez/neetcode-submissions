class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # idea: hash map where the key is the difference from target and the value is the index
        diff_dict = {}
        for i, num in enumerate(nums):
            diff = target - num
            diff_dict[diff] = i

        for j, num in enumerate(nums):
            if num in diff_dict:
                i = diff_dict[num]
                if i!=j:
                    results = [i,j]
                    return [min(results), max(results)]

        return []
