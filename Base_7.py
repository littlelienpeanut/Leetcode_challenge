class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        
        output = ''
        flag = ''
        if num < 0:
            num = abs(num)
            flag = '-'
        
        
        
        while num != 0:
            output = str(num % 7) + output
            num = int(num/7)

        return flag + output


