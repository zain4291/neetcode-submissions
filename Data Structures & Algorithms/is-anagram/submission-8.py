class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}

        for i in s:
            hash1[i] = 1 + hash1.get(i, 0)
        for i in t:
            hash2[i] = 1 + hash2.get(i, 0)    
        return hash1 == hash2