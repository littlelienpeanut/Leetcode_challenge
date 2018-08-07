class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vo = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0, 'A':0, 'E':0, 'I':0, 'O':0, 'U':0}
        s = list(s)
        i = 0
        j = len(s)-1
        while (i < j):
            while (i < j and s[i] not in vo):
                i += 1
            
            while (i < j and s[j] not in vo):
                j -= 1
            
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        
        return ''.join(s)
        
