class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans,slow = [],0
        num=1
        for ign_num in range(len(nums)):
            front = (nums[0:ign_num])
            behind = (nums[ign_num+1:len(nums)])
            front+=behind 
            for i in range(len(front)):
                num*=front[i]
            ans.append(num)
            num=1

        return(ans)