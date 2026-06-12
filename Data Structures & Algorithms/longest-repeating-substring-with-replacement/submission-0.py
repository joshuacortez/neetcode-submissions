class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        counter = {}
        max_len = 0
        for right in range(len(s)):
            counter[s[right]] = counter.get(s[right], 0) + 1
            max_char = max(counter, key=counter.get)
            max_freq = counter[max_char]
            window_len = right - left + 1

            # replacing everything else except the most frequent one
            num_replace = window_len - max_freq

            while num_replace > k:
                counter[s[left]] -= 1
                left += 1

                max_char = max(counter, key=counter.get)
                max_freq = counter[max_char]
                window_len = right - left + 1

                # replacing everything else except the most frequent one
                num_replace = window_len - max_freq

            max_len = max(max_len, window_len)

        return max_len

            