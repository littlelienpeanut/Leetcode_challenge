class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        cnt = 1
        output = 0
        num = len(s) - 1

        for i in letter:
            dict.update({i:cnt})
            cnt += 1

        for i in s:
            output += dict[i]*pow(26, num)
            num -= 1

        return output
        
