from collections import Counter
class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if 'LLL' not in s and s.count('A') < 2:
            return True

        else:
            return False
        
