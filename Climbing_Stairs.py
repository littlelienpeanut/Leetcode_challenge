class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        table = {}

        def sub(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            
            if (n-1) not in table:
                table.update({(n-1):sub(n-1)})
            
            if (n-2) not in table:
                table.update({(n-2):sub(n-2)})
            
            
            return table[n-1] + table[n-2]
        
        return sub(n)
        
