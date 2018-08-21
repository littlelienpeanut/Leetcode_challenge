from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        output = []
        dict_p = Counter(p)
        dict_s = Counter(s[:len(p)-1])
        for i in range(len(p)-1, len(s)):
            dict_s[s[i]] += 1
            if dict_p == dict_s:
                output.append(i-len(p)+1)
            
            dict_s[s[i-len(p)+1]] -= 1
            
            if dict_s[s[i-len(p)+1]] == 0:
                del dict_s[s[i-len(p)+1]]
            
            
        
        return output
