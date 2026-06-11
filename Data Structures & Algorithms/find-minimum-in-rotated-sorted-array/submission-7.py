class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        j = len(nums) - 1

        minval = min(nums[l], nums[j])
        while l <= j:
            # this means its sorted
            if nums[l] <= nums[j]:
                minval = min(nums[l], minval)

            m = (l + j) // 2
            minval = min(minval, nums[m])
            if nums[m] >= nums[l]:
                # search right
                l = m + 1
            else:
                # search left
                j = m - 1

        return minval
        