class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainders = {}
        for i, num in enumerate(nums):
            if num in remainders.keys():
                remainder_idx = remainders[num]
                return [remainder_idx, i]
            remainder = target - num
            remainders[remainder] = i
