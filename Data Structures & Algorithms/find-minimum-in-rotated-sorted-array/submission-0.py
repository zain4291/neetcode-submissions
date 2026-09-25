class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = nums[0]

        for i in nums:
            n = min(n, i)

        return n

        