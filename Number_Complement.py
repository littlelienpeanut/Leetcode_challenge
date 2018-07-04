class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        b_num = bin(num)[2:]
        b_num = b_num[::-1]
        output = 0

        for i in range(0, len(b_num), 1):
            if b_num[i] == '0':
                output += pow(2, i)

        return output
