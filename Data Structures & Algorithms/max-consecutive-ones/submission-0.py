class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive = 0
        counter = 0

        for num in nums:
            if num == 1:
                counter += 1
                if counter > max_consecutive:
                    max_consecutive = counter
            else:
                counter = 0

        return max_consecutive