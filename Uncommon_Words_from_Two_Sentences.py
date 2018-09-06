from collections import Counter
class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        A = A.split(' ')
        B = B.split(' ')
        A = A+B
        A = Counter(A)
        output = []
        for key, val in A.items():
            if val == 1:
                output.append(key)
        
        return output
