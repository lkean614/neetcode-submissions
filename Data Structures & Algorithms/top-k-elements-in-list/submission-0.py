from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num = Counter(nums)
        max_k_item = [(val,index)for index,val in num.items()]
        max_tuples = heapq.nlargest(k,max_k_item)
        max_k = [(index)for (val,index) in max_tuples]
        return max_k