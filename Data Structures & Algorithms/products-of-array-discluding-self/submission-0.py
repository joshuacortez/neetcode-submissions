class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)
        for i, num in enumerate(nums):
            for j in range(len(nums)):
                if i != j:
                    result[i] *= nums[j]

        return result
            
        