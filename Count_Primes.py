class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        \
        s = [1]*n
        s[0] = s[1] = 0
        for i in xrange(2, int(n**1/2)+1):
            if s[i] != 0:
                for j in range(i*2, n, i):
                    s[j] = 0
        
        return sum(s)
