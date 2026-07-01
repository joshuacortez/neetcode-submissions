class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_chars = {}
        for i, char in enumerate(t):
            if char not in t_chars:
                t_chars[char] = []
            t_chars[char].append(i)

        curr_i = -1
        for char in s:
            if char not in t_chars:
                return False
            
            is_subsequence = False
            char_indices = t_chars[char]
            for char_index in char_indices:
                if char_index > curr_i:
                    curr_i = char_index
                    is_subsequence = True
                    break
            
            if not is_subsequence:
                return False

        return True

