class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1

        if not nums:
            return -1

        while i <= j:
            if nums[i] == target:
                return i
            if nums[j] == target:
                return j
            mid_idx = (i + j) // 2
            mid_num = nums[mid_idx]
            if mid_num == target:
                return mid_idx 
            elif mid_num > target:
                j = mid_idx -1 
            else:
                i = mid_idx + 1
    
        return -1

        