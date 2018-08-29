class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        output = ''
        if strs == []:
            return output
        
        for i in range(len(strs[0])):
            tmp = strs[0][i]
            for word in strs:
                try:
                    if word[i] != tmp:
                        return output
                
                except:
                    return output
            
            output += tmp
        
        return output
        
