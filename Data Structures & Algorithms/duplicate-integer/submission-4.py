class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums)==0:
            return False

        role = nums[0]
        nums.sort()

        for i in nums[1:]:
            if i == role:
                return True
            else:
                role = i
        return False