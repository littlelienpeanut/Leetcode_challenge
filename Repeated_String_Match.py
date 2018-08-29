class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if A.find(B) != -1:
            return 1
        
        for times in range(2, 10001):
            tmp = A*times
            
                
            if tmp.find(B) != -1:
                return times
            
            if len(tmp) > len(B)*2:
                return -1
        
        return -1
        
