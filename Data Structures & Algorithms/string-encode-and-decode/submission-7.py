class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "é"
        else:
            return "ñ".join(strs)
    def decode(self, s: str) -> List[str]:
        if s == "é":
            return []
        decoded = s.split("ñ")
        return decoded