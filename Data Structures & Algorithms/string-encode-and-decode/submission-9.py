class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "" 

        encoded = ""
        for s in strs:
            encoded += f"{s}é"

        return encoded

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []

        decoded = []
        current_str = ""
        for char in s:
            if char == "é":
                decoded.append(current_str)
                current_str = ""
            else:
                current_str += char

        return decoded