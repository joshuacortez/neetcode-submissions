class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        taken_counter = {num:False for num in nums}
        for num in nums:
            if taken_counter[num]:
                return True
            taken_counter[num] = True
        return False
