class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        
        tmp = 0
        root = int(num**0.5)
        for i in range(1, root+1):
            if num % i == 0:
                tmp += i
                tmp += num//i
                
        if (root)**2 == num:
            tmp -= root
            
        return tmp == num*2
        
