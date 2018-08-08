class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0:
            return False
        n = num
        while (n**2 > num):
            n = (n + num/n) // 2
        
        return n**2 == num
