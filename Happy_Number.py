class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        d = set()
        d.add(n)
        
        while (n != 1):
            tmp = 0
            for i in str(n):
                tmp += int(i)**2
            
            n = tmp
            if n in d:
                return False
            
            else:
                d.add(n)
            
        return True
        
