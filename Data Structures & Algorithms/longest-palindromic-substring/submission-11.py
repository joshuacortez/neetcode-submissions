class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        def expanding_twopointers(s, left, right) -> str:
            """
            Returns the longest palindrome found
            """
            while left >= 0 and right <= len(s) - 1:
                if s[left] != s[right]:
                    break
               
                left-=1
                right+=1

            # we get the indices before the while loop exited
            final_left = left + 1
            final_right = right - 1

            found_palindrome = s[final_left:final_right+1]

            return found_palindrome

        best_palindrome = ""
        # odd case
        for i in range(len(s)):
            left = i
            right = i
            found_palindrome = expanding_twopointers(s, left, right)
            if len(found_palindrome) > len(best_palindrome):
                best_palindrome = found_palindrome
        
        # even case
        for i in range(len(s)):
            left = i
            right = i+1
            found_palindrome = expanding_twopointers(s, left, right)
            if len(found_palindrome) > len(best_palindrome):
                best_palindrome = found_palindrome

        return best_palindrome

        