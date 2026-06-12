class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        current_window = set()
        longest_len = 0

        for right in range(len(s)):
            char = s[right]
            if char not in current_window:
                current_window.add(char)
                longest_len = max(longest_len, len(current_window))
            else:
                while (s[left] != char):
                    if s[left] in current_window:
                        current_window.remove(s[left])
                    left += 1
                # this is important because you want left to be outside the duplicate
                left += 1

        return longest_len