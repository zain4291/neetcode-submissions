class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = sorted(nums)
        trip = []
        fix = 0

        while fix < len(arr) - 1:
            if fix > 0 and arr[fix] == arr[fix - 1]:
                
                fix+=1
                continue
            
            l = fix + 1
            r = len(arr) - 1

            while l < r:
                if arr[l] + arr[r] + arr[fix] < 0:
                    l+=1
                elif arr[l] + arr[r] + arr[fix] > 0:
                    r-=1
                else:
                    trip.append([arr[l], arr[r], arr[fix]])
                    l+=1
                    r-=1

                    while l < r and arr[l] == arr[l - 1]:
                        l+=1
                    while r > l and arr[r] == arr[r + 1]:
                        r-=1
            fix+=1
        return trip

        