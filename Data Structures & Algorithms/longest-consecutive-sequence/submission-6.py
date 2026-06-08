class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seen_nums = set(nums)
        max_len = 1
        for num in seen_nums:
            if num-1 not in seen_nums:
                print(f"{num} is a seed")
                current_len = 1
                while (num+current_len) in seen_nums:
                    print(f"{num+current_len} is available")
                    current_len += 1
                if current_len > max_len:
                    max_len = current_len
        return max_len