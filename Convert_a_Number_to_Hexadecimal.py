class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        output = ''
        dict_hex = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
        
        if num < 0:
            while (len(output)<8):
                output = dict_hex[num % 16] + output
                num = int(num / 16)
        
        else:
            while (num != 0):
                output = dict_hex[num % 16] + output
                num = int(num / 16)
        
        return output
