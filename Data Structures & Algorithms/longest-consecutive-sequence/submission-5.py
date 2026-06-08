class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seen_nums = set(nums)
        counts = {num:1 for num in seen_nums}
        max_count = 1
        for num in seen_nums:
            i = 1
            while (num-i) in seen_nums:
                counts[num-i] += 1
                if counts[num-i] > max_count:
                    max_count = counts[num-i]
                i += 1

        return max_count
         
        