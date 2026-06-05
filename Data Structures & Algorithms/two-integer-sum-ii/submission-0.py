class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        fast = len(numbers)-1
        i=0
        while i <= len(numbers):
            current_num = numbers[i] + numbers[fast]
            if current_num == target:
                return([i+1,fast+1])
            if current_num > target:
                fast-=1
            if current_num < target:
                i+=1