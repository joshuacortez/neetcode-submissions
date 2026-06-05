class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)
        for i in range(len(nums)):
            rest = nums[(i+1):] + nums[:i] 
            for r in rest:
                result[i] *= r
        return result
            
        