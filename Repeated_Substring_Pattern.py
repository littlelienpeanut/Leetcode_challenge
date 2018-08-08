class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return Fasle
        
        tmp = (s+s)[1:-1]
        return tmp.find(s) != -1
