class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        n_alphabet = ord("z") - ord("a") +1
        for i, s in enumerate(strs):
            s_fingerprint = [0] * n_alphabet
            for char in s: 
                s_index = ord(char) - ord("a")
                s_fingerprint[s_index] += 1
            s_fingerprint = tuple(s_fingerprint)
            
            if s_fingerprint not in anagram_dict.keys():
                anagram_dict[s_fingerprint] = [s]
            else:
                anagram_dict[s_fingerprint].append(s)
        return list(anagram_dict.values())
        