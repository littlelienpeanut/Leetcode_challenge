class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        tmp = set()
        for i in range(0, int(math.sqrt(c))+1):
            tmp.add(i**2)
        
        for num in tmp:
            if c - num in tmp:
                return True
        return False
            
            
