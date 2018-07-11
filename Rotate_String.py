class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) > len(B):
            return False

        A += A
        if A.find(B) != -1:
            return True

        else:
            return False
        
