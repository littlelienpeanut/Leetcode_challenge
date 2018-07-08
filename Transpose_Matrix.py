class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        output = []

        for u in range(len(A[0])):
            tmp = []
            for v in range(len(A)):
                tmp.append(A[v][u])

            output.append(tmp)

        return output
