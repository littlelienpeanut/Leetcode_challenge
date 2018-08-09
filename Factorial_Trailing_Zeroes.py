class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while (n > 0):
            n /= 5
            cnt += n
        
        return cnt
        
