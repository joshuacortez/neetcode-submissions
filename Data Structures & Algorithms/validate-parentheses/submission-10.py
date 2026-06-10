class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        reverse_mapping = {
            ")":"(",
            "}":"{",
            "]":"[",
        }
            
        stack = []
        for char in s:
            if char not in reverse_mapping.keys():
                stack.append(char)
            else:
                if not stack or (stack[-1] != reverse_mapping[char]):
                    return False
                stack.pop()
        
        return not stack