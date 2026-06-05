class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,0
        res = prices[r]-prices[l]
        
        for i in range(len(prices)):
            if prices[i] < prices[l]:
                l=i
                r=i
            if prices[i]>prices[r]:
                r=i
            current = prices[r]-prices[l]
            res = max(res,current)
        print(l)
        print(r)
        return res