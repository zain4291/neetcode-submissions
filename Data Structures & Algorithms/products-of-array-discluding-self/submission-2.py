class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zcnt = 1, 0
        for num in nums:
            if num:
                prod*=num
            else:
                zcnt+=1
        if zcnt > 1: return [0] * len(nums)

        res = [0] * len(nums)
        for i,c in enumerate(nums):
            if zcnt: res[i] = 0 if c else prod
            else: res[i] = prod // c
        return res
        
            