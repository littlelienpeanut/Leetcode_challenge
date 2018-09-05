# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 0, n
        while (True):
            if isBadVersion(n) and isBadVersion(n-1) == False and isBadVersion(n+1):
                return n
            
            if isBadVersion(n):
                r = n
            
            else:
                l = n
            
            n = (l + r) // 2
            
