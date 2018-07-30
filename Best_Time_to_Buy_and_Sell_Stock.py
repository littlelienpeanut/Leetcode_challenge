class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if len(prices) <= 1:
            if prices == []:
                return 0
            
            else:
                return 0
        
        output = 0
        for i in range(len(prices)-1):
            if prices[i] >= prices[i+1]:
                pass
            
            else:
                now = max(prices[i+1:]) - prices[i]
                output = max(output, now)
        
        return output
        
        
