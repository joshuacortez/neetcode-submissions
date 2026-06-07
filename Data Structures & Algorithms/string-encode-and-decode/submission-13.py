class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
         
        encoded = ""
        for s in strs:
            encoded += f"{len(s)}#{s}"

        return encoded
        
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        decoded = []
        i = 0
        len_str = ""
        while i < len(s):
            if s[i] == "#":
                start_str_idx = i+1
                end_str_idx = start_str_idx + int(len_str)
                encoded_str = s[start_str_idx:end_str_idx]

            
                decoded.append(encoded_str)
                i = end_str_idx 
                len_str = ""
            else:
                len_str += s[i]
                i += 1
        

        return decoded
