class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        ans = nums[-1]

        while l <= r:
            mid = (l+r)//2
            if nums[mid] < ans and nums[mid] < nums[-1]:
                r = mid - 1
                ans = min(ans,nums[mid])
            else:
                l = mid + 1
        return ans