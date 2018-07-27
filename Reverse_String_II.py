class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        output = ''
        for i in range(0, len(s), 2*k):
            tmp = list(s[i:i+k])[::-1]
            output += ''.join(tmp)
            output += s[i+k:(i+2*k)]

        return output
        
