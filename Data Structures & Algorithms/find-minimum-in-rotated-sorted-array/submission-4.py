class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        min_val = min(nums[l], nums[r])
        while l < r:
            mid_idx = (l + r) // 2 
            mid_val = nums[mid_idx]
            min_val = min(min_val, mid_val)

            premid_val = nums[mid_idx - 1]
            postmid_val = nums[mid_idx + 1] 
            # found a breakpoint
            if (mid_val<premid_val) and (mid_val<postmid_val):
                return min_val
            elif (mid_val>premid_val) and (mid_val>postmid_val):
                return postmid_val
            elif nums[l] < mid_val:
                l = mid_idx + 1
            elif mid_val < nums[r]:
                r = mid_idx - 1

        return min_val


            
        