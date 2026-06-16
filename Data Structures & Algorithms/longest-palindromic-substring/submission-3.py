class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]

        def is_palindrome(s: str, left: int, right: int) -> bool:
            """
            Starting from indices left and right, return True if s is a palindrome
            otherwise return False
            """
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            
            return True
        
        from itertools import combinations
        def valid_combinations(indices: List[int]) -> List[List[int]]:
            """
            Return pairs of indices (left,right) where left > right
            """
            return [(left,right) for (left,right) in combinations(indices,2) if left<right]

        char_mapping = {}
        for i, char in enumerate(s):
            if char not in char_mapping:
                char_mapping[char] = [i]
            else:
                char_mapping[char].append(i)
        
        best_palindrome = ""
        for char in char_mapping:
            indices = char_mapping[char]
            if len(indices) < 2:
                continue

            # key insight: if the shortest substr isn't a palindrome, then the 
            # largest substr isn't a palindrome
            candidates = valid_combinations(indices)
            for (left, right) in candidates:
                palindrome_cand = s[left:right+1]
                len_candidate = right - left + 1
                if len_candidate >= len(best_palindrome):
                    result = is_palindrome(s, left, right)
                    if result and len(palindrome_cand) > len(best_palindrome):
                        best_palindrome = palindrome_cand

        return best_palindrome
                
            