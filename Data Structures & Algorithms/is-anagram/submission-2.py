class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts1 = {}
        for letter in s:
            if letter not in counts1.keys():
                counts1[letter] =1
            counts1[letter] += 1

        counts2 = {}
        for letter in t:
            if letter not in counts2.keys():
                counts2[letter] = 1
            counts2[letter] += 1

        return counts1 == counts2
