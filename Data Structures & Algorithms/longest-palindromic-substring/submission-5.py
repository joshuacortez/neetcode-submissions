class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        def expanding_twopointers(s, left, right) -> str:
            """
            Returns the longest palindrome found
            """
            found_palindrome = ""
            while left >= 0 and right <= len(s) - 1:
                if s[left] != s[right]:
                    break
                else:
                    found_palindrome = s[left:right+1]
                left-=1
                right+=1

            return found_palindrome

        best_palindrome = ""
        # odd case
        for i in range(len(s)-1):
            left = i
            right = i
            found_palindrome = expanding_twopointers(s, left, right)
            if len(found_palindrome) > len(best_palindrome):
                best_palindrome = found_palindrome
        
        # even case
        for i in range(len(s)-1):
            left = i
            right = i+1
            if right >= len(s):
                continue
            found_palindrome = expanding_twopointers(s, left, right)
            if len(found_palindrome) > len(best_palindrome):
                best_palindrome = found_palindrome

        return best_palindrome
