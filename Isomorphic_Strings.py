from collections import Counter
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return [s.find(a) for a in s] == [t.find(b) for b in t]
        
