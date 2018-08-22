class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        tmp = {}
        tmp_value = {}
        s = str.split(' ')
        if len(s) != len(pattern):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] not in tmp:
                if s[i] in tmp_value:
                    return False
                tmp_value.update({s[i]:0})
                tmp.update({pattern[i]:s[i]})
            
            
            else:
                if tmp[pattern[i]] != s[i]:
                    return False
                
        return True
                
