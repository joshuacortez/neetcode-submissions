class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        # pure overwriting approach
        # no need to retain the original values
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
            print(i)
            print(i)
            print(nums)
        return k