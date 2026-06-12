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
                left += 1
                current_window.add(char)

        return longest_len