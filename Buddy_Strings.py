from collections import Counter
class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        a, b = Counter(A), Counter(B)
        cnt = 0
        
        if a != b:
            return False
        
        if A == B and (len(list(a.keys())) <= len(A) and len(A) <= len(list(a.keys()))):
            return False
        
        for i in range(len(A)):
            if A[i] != B[i]:
                cnt += 1
                
        return cnt == 2 or A == B
        
        
