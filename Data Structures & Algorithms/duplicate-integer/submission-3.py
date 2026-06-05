class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums)==0:
            return False
        role = nums[0]
        time = 0
        nums.sort()
        for i in nums:
            if i == role:
                print(1)
                time+=1
            else:
                print(2)
                role = i
                time=1
            if time >1:
                print(3)
                return True
        return False