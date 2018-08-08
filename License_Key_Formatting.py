class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = list(S)[::-1]
        ind = 0
        cnt = 0
        output = ''
        
        while (ind < len(S)):
            if S[ind] == '-':
                pass
            
            else:
                cnt += 1
                output = S[ind].upper() + output
                if cnt == K:
                    output = '-' + output
                    cnt = 0
            
            ind += 1
        
        if output == '':
            return ''
        
        if output[0] == '-':
            return output[1:]
        
        return output
                
                
                
                
