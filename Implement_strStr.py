class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        #return haystack.find(needle)
        if len(needle) > len(haystack):
            return -1
        
        if haystack == needle:
            return 0
        
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        
        return -1
        
