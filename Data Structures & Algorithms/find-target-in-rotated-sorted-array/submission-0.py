class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        # first find the pivot, which is the same as the minimum
        if nums[l] <= nums[r]:
            min_val = nums[l]
            min_i = l
        else:
            min_val = nums[r]
            min_i = r

        while l <= r:
            if nums[l] <= nums[r]:
                if nums[l] < min_val:
                    min_val = nums[l]
                    min_i = l
                    break
            
            m = (l+r) // 2
            if nums[m] < min_val:
                min_val = nums[m]
                min_i = m
            if nums[l] <= nums[m]:
                # search right
                l = m + 1
            else:
                r = m - 1
        
        # do binary search twice, one on each sublist
        indices1 = [0,min_i-1]
        indices2 = [min_i, len(nums)-1]

        for indices in [indices1, indices2]:
            if len(set(indices)) == 1:
                if nums[indices[0]] == target:
                    return indices[0]
                continue
            
            l, r = indices
            if (target < nums[l]) or (target > nums[r]):
                continue

            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    return m
                elif target > nums[m]:
                    # search right
                    l = m + 1
                else:
                    # search left
                    r = m - 1
            
        return -1 
