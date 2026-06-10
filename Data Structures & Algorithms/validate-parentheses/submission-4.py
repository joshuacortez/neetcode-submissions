class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        start_symbols = set(["(", "{", "["])

        reverse_mapping = {
            ")":"(",
            "}":"{",
            "]":"[",
        }
            
        stack = []
        for char in s:
            if char in start_symbols:
                stack.append(char)
            if char in reverse_mapping.keys():
                if not stack:
                    return False
                else: 
                    if stack[-1] == reverse_mapping[char]:
                        stack.pop()
                    else:
                        return False
        
        if stack:
            return False
        else:
            return True