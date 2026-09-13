
def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    min_price = prices[0]
    profit = 0
    for i in range(1,len(prices)):
        if min_price > prices[i]:
            min_price = prices[i]
        
        profit = max(profit ,   prices[i] - min_price)
    
    return profit