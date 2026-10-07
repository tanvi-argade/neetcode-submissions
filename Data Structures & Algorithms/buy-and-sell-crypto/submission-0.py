class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        minprice=prices[0]

        for i in prices:
            if i<minprice:
                minprice=i
            currentprofit=i-minprice
            if currentprofit>profit:
                profit=currentprofit
        return profit