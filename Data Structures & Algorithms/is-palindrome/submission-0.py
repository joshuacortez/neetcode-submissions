class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)
        is_palindrome = True
        i = 0
        j = len(s) - 1
        while i < j:
            start = s[i].lower()
            end = s[j].lower()
            if not start.isalnum():
                i += 1
                continue
            if not end.isalnum():
                j -= 1
                continue
            if start != end:
                print(i, j)
                print(start, end)
                return False
            i += 1
            j -= 1
        return True