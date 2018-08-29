class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s)-1
        while (left<right):
            if s[left] != s[right]:
                a, b = s[left:right], s[left+1:right+1]
                return a == a[::-1] or b == b[::-1]
            left += 1
            right -= 1
        
        return True
        
