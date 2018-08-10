class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split(' ')
        cnt = 0
        for c in s:
            if c != '':
                cnt += 1
                
        return cnt
        
