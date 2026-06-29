class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
            
        i = 0
        j = len(nums) - 1

        # this reminds me of the dutch flag approach
        while i < j:
            if nums[j] == val:
                j -= 1
            elif nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            else:
                i += 1
            print(nums)
            print(i)
            print(j)

        if i == j == 0:
            return 0

        k = min(i,j) + 1
        return k
    