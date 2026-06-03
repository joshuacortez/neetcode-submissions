class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            print(sorted_s)
            if sorted_s not in anagram_dict.keys():
                anagram_dict[sorted_s] = [s]
            else:
                anagram_dict[sorted_s].append(s)

        return list(anagram_dict.values())
        