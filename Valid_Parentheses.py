class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tmp = {'[':']', '{':'}', '(':')'}
        stack = []
        for ch in s:
            if ch not in tmp:
                if stack == []:
                    return False
                
                if tmp[stack[-1]] != ch:
                    return False
                
                else:
                    try:
                        stack.pop(-1)
                    
                    except:
                        return False
            else:
                stack.append(ch)
        
        if stack:
            return False
        
        else:
            return True
                
        
            
        
