class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0

        for i in range(len(s)-1):
            if dict[s[i]] < dict[s[i+1]]:
                res -= dict[s[i]] ## if the number is smaller than the number behind it, it will be negative
            else:
                res += dict[s[i]]

        res += dict[s[len(s)-1]]
        return res
