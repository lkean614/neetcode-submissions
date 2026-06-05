class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        max_pro = 0

        while l<r and r<len(prices):
            current = prices[r]-prices[l]
            if prices[r]>prices[l]:
                max_pro = max(max_pro,current)
            else:
                l=r
            r+=1
        return max_pro