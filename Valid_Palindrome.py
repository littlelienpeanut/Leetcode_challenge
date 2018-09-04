class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = filter(str.isalnum, str(s)).lower()
        return s==s[::-1]
