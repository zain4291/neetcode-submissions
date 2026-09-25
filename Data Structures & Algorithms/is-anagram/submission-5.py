class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}

        for c in s:
            hash1[c] = 1 + hash1.get(c, 0)
        for c in t:
            hash2[c] = 1 + hash2.get(c, 0)

        return hash1 == hash2
        