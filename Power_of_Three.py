import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while (n > 1):
            if n % 3 == 0:
                n /= 3
            
            else:
                return False
        
        return n == 1
        
        
        
