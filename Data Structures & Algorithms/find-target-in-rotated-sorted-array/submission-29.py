class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        if nums[l] == target:
            return l
        if nums[r] == target:
            return r

        while l < r:
            mid = l + (r - l)//2

            
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            if nums[mid] == target:
                return mid
            if nums[l] < target:

                if nums[l] < target < nums[mid]:
                    l+=1
                else:
                    r-=1
            else:
                if target < nums[mid] < nums[r]:
                    r-=1
                else:
                    l+=1
        return -1        