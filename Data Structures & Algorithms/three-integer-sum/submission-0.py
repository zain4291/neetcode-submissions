class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = sorted(nums)
        fix = 0
        trip = []

        while fix < len(arr) - 1:
            if fix > 0 and arr[fix] == arr[fix - 1]:
                fix += 1
                continue

            l = fix + 1
            r = len(arr) - 1
        
            while l < r:
                if arr[l] + arr[r] + arr[fix] < 0:
                    l = l + 1
                elif arr[l] + arr[r] + arr[fix] > 0:
                    r = r - 1
                else:
                    trip.append([arr[l], arr[r], arr[fix]])
                    l+=1
                    r-=1

                    while arr[l] == arr[l - 1] and l < r:
                        l+=1
                    while arr[r] == arr[r + 1] and r > l:
                        r-=1
            fix+= 1
        return trip