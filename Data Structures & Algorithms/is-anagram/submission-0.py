class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sf = sorted(s)
        tf = sorted(t)

        return sf == tf

            

        


        