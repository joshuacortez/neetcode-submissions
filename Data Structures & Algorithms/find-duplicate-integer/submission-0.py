class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            if counts[num] >= 2:
                return num
        

        