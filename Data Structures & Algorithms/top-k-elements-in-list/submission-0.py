class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashS = {}

        for i in nums:
            if i in hashS:
                hashS[i] += 1
            else:
                hashS[i] = 1

        newS = dict(sorted(hashS.items(), key=lambda item: item[1], reverse = True))

        newSl = list(newS)
        l = []
        for i in range(k):
            l.append(newSl[i])
        return l


         