class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num = list(set(bin(n)[3:]))
        for i in num:
            if i == '1':
                return False
        return n > 0
        
