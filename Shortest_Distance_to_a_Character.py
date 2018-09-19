class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        p, result = [], []
        for i in range(len(S)):
            if S[i] == C:
                p.append(i)
        
        for i in range(len(S)):
            result.append(min([abs(ind-i) for ind in p]))
            
        
        return result
                
