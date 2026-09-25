class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashA = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for i in s:
                count[ord(i) - ord('a')] += 1

            hashA[tuple(count)].append(s)
        return list(hashA.values())