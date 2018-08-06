from collections import Counter
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = bin(n)[2:]
        n = Counter(n)
        return n['1']
