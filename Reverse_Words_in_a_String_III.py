class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        output = ''
        s = s.split( )
        for word in s:
            output += word[::-1]
            output += ' '


        return output[:-1]
