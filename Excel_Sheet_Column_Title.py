class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
            
        tmp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        output = ''
        tmp_dict = {}
        for i, al in enumerate(tmp):
            tmp_dict.update({i:al})
        
        while (n > 0):
            output = tmp_dict[((n-1)%26)] + output
            n = (n-1)//26
        
        return output
        
