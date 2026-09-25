class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash1 = {}
        hash2 = {}

        for i in s:
            hash1[i] = 1 + hash1.get(i, 0)

        for j in t:
            hash2[j] = 1 + hash2.get(j, 0)

        return hash1 == hash2
