# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = r = 0
        while (guess(n) != 0):
            if guess(n) == -1:
                r = n
                n = (r+l) // 2

            else:
                l = n
                n = (r+l) // 2
    
        return n
        
