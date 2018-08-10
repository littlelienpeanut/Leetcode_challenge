class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        cnt = 1
        while (n >= 0):
            n -= cnt
            cnt += 1
        
        return cnt -2
